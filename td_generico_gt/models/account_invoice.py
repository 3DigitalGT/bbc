# -*- coding: utf-8 -*-

from odoo import fields, api, models
from odoo.exceptions import UserError
import re
import uuid

class account_journal(models.Model):
    _inherit = "account.journal"

    doc_type = fields.Selection(selection=[
        ("RECI", "Recibo"),
        ("FACT", "Factura"),
        ("FCAM", "Factura Cambiaria"),
        ("FPEQ", "Factura Pequeño Contribuyente"),
        ("FCAP", "Factura Cambiaria Pequeño Contribuyente"),
        ("FESP", "Factura Especial"),
        ("RDON", "Recibio Donación"),
        ("REC", "Factura Pequeño Contribuyente"),
        ("NABN", "Nota de Abono"),
        ("NCRE", "Nota de Credito"),
        ("NDEB", "Nota de Debito"),
    ]
        , string="Tipo Documento")

class Invoice(models.Model):
    _inherit = "account.invoice"

    doc_serie = fields.Char("Serie")
    doc_type = fields.Selection(selection=[
            ("RECI","Recibo"),
            ("FACT","Factura"),
            ("FCAM","Factura Cambiaria"),
            ("FPEQ","Factura Pequeño Contribuyente"),
            ("FCAP", "Factura Cambiaria Pequeño Contribuyente"),
            ("FESP", "Factura Especial"),
            ("RDON", "Recibio Donación"),
            ("REC", "Factura Pequeño Contribuyente"),
            ("NABN", "Nota de Abono"),
            ("NCRE", "Nota de Credito"),
            ("NDEB", "Nota de Debito"),
        ]
        ,string="Tipo Documento")
    doc_number = fields.Char("Numero")
    amount_tax_total = fields.Monetary(string='Total Impuestos',
        store=True, readonly=True, compute='_compute_amount')
    amount_retained_tax_total = fields.Monetary(string='Total Impuesto Retenido',
        store=True, readonly=True, compute='_compute_amount')
    amount_retained_vat_total = fields.Monetary(string='IVA Retenido',
                                                store=True, readonly=True, compute='_compute_amount')
    amount_retained_isr_total = fields.Monetary(string='ISR Retenido',
                                                store=True, readonly=True, compute='_compute_amount')
    amount_grand_total = fields.Monetary(string='Gran Total',
                                                store=True, readonly=True, compute='_compute_amount')
    #reference = fields.Char(string = "Referencia", compute = "_set_reference")

    @api.one
    def _set_reference(self):
        for inv in self:
            if inv.type in ('out_invoice', 'out_refund'):
                inv.doc_type = inv.journal_id.doc_type
                inv.doc_number = inv.number
            inv.reference = '%s-%s' % (inv.doc_serie,inv.doc_number)


    @api.constrains('doc_serie','doc_number')
    @api.one
    def _check_duplicate_supplier_reference(self):
        for invoice in self:
            # refuse to validate a vendor bill/credit note if there already exists one with the same reference for the same partner,
            # because it's probably a double encoding of the same bill/credit note
            # only if the two invoices are validated.
            self.ensure_one()
            if invoice.type in ('in_invoice', 'in_refund') and invoice.reference:
                res = self.env['account.invoice'].search([
                    ('type', '=', invoice.type),
                    ('doc_serie', '=', invoice.doc_serie),
                    ('doc_number', '=', invoice.doc_number),
                    ('company_id', '=', invoice.company_id.id),
                    ('partner_id', '=', invoice.partner_id.id),
                    ('doc_type', '=', invoice.doc_type),
                    ('id', '!=', invoice.id),
                    ('state', 'in', ('paid','open','in_payment'))])
                if res:
                    raise UserError(
                        "Duplicated vendor reference detected. You probably encoded twice the same vendor bill/credit note.")

    @api.multi
    def invoice_validate(self):
        for invoice in self.filtered(lambda invoice: invoice.partner_id not in invoice.message_partner_ids):
            invoice.message_subscribe([invoice.partner_id.id])

            # Auto-compute reference, if not already existing and if configured on company
            #if not invoice.reference and invoice.type == 'out_invoice':
            invoice.reference = invoice._get_computed_reference()

            # DO NOT FORWARD-PORT.
            # The reference is copied after the move creation because we need the move to get the invoice number but
            # we need the invoice number to get the reference.
            if invoice.name:
                invoice.move_id.ref = invoice.name
            else:
                desc = ''
                if invoice.type == 'out_invoice':
                    desc = 'Venta a '
                if invoice.type == 'out_refund':
                    desc = 'Nota Credito a '
                if invoice.type == 'in_invoice':
                    desc = 'Compra a '
                if invoice.type == 'in_refund':
                    desc = 'Devolucion de '
                #invoice.move_id.ref = desc + invoice.partner_id.legal_name + ' con documento ' + invoice.doc_type + ' ' + invoice.reference
        self._check_duplicate_supplier_reference()

        return self.write({'state': 'open'})


    @api.multi
    def _get_computed_reference(self):
        self.ensure_one()
        if self.type in ('out_invoice', 'out_refund'):
            if self.company_id.invoice_reference_type == 'invoice_number':
                seq_suffix = self.journal_id.sequence_id.suffix or ''
                regex_number = '.*?([0-9]+)%s$' % seq_suffix
                exact_match = re.match(regex_number, self.number)
                if exact_match:
                    identification_number = int(exact_match.group(1))
                else:
                    ran_num = str(uuid.uuid4().int)
                    identification_number = int(ran_num[:5] + ran_num[-5:])
            self.doc_type = self.journal_id.doc_type
            self.doc_serie = self.journal_id.sequence_id.prefix or ''
            self.doc_number = str(identification_number % 97).rjust(self.journal_id.sequence_id.padding, '0')
            return '%s%s' % (self.doc_serie,self.doc_number)
        else:
            return '%s-%s' % (self.doc_serie, self.doc_number)

    @api.multi
    def action_invoice_draft(self):
        pass

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type')
    def _compute_amount(self):
        round_curr = self.currency_id.round
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)
        #self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids)
        self.amount_tax =  self.amount_tax_total = self.amount_retained_tax_total = 0
        for line in self.tax_line_ids:
            self.amount_tax += line.amount_total
            self.amount_tax_total += abs(line.amount_total)
            if line.amount_total < 0:
                self.amount_retained_tax_total += abs(line.amount_total)
        self.amount_total = self.amount_untaxed + self.amount_tax #- self.amount_retained_tax_total
        self.amount_grand_total = self.amount_untaxed + self.amount_tax + abs(self.amount_retained_tax_total)
        amount_total_company_signed = self.amount_total
        amount_untaxed_signed = self.amount_untaxed
        if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
            currency_id = self.currency_id
            amount_total_company_signed = currency_id._convert(self.amount_total, self.company_id.currency_id,
                                                               self.company_id,
                                                               self.date_invoice or fields.Date.today())
            amount_untaxed_signed = currency_id._convert(self.amount_untaxed, self.company_id.currency_id,
                                                         self.company_id, self.date_invoice or fields.Date.today())
        sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
        self.amount_total_company_signed = amount_total_company_signed * sign
        self.amount_total_signed = self.amount_total * sign
        self.amount_untaxed_signed = amount_untaxed_signed * sign

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    line_total = fields.Monetary(string='Importe',
                                                store=True, readonly=True, compute='_compute_price')

    @api.one
    @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
        'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
        'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price(self):
        currency = self.invoice_id and self.invoice_id.currency_id or None
        price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
        self.line_total = price * self.quantity
        taxes = False
        if self.invoice_line_tax_ids:
            taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id, partner=self.invoice_id.partner_id)
        self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.quantity * price
        self.price_total = taxes['total_included'] if taxes else self.price_subtotal
        if self.invoice_id.currency_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
            currency = self.invoice_id.currency_id
            date = self.invoice_id._get_currency_rate_date()
            price_subtotal_signed = currency._convert(price_subtotal_signed, self.invoice_id.company_id.currency_id, self.company_id or self.env.user.company_id, date or fields.Date.today())
        sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
        self.price_subtotal_signed = price_subtotal_signed * sign