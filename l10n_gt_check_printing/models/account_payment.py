# -*- coding: utf-8 -*-

from odoo import models, api, fields

class res_partner_bank(models.Model):
    _inherit = 'res.partner.bank'

    def name_get(self):
        result = []
        for record in self:
            bank = (record.bank_id.name or '')
            account = (record.acc_number or '')
            name = bank + ' - ' + account
            result.append((record.id, name))
        return result

class account_journal(models.Model):
    _inherit = 'account.journal'

    account_check_printing_layout = fields.Selection(string="Formato Cheque", required=True,
                                                     help="Seleccione el formato que desea utilizar para imprmir sus cheques.\n"
                                                          "Para deshabilitar la función, seleccione 'Ninguno'.",
                                                     selection=[
                                                         ('disabled', 'Ninguno'),
                                                         ('action_print_check_voucher', 'Voucher'),
                                                         ('action_print_check_format', 'Formato'),
                                                     ],
                                                     default="action_print_check_format")


class account_payment(models.Model):
    _inherit = "account.payment"

    document_reference = fields.Char(compute = '_get_document_reference', string="Referencia", store=True)

    @api.onchange('payment_method_id')
    def _payment_method_change(self):
        if self.payment_method_id.code == 'TRA':
            self.show_partner_bank_account = True

    @api.depends('check_number')
    def _get_document_reference(self):
        for record in self:
            record.document_reference = record.check_number

    def do_print_checks(self):
        self.cheque_formate_id = self._get_check_formate()
        if self:
            if self.journal_id.account_check_printing_layout != 'disabled':  #Si no hay definido formato en el journal, buscar el predeterminado para la empresa
                check_layout = self.journal_id.account_check_printing_layout
            else:
                check_layout = self[0].company_id.account_check_printing_layout
            if check_layout != 'disabled' and self[0].journal_id.company_id.country_id.code == 'GT':
                self.write({'state': 'sent'})
                if self.journal_id.account_check_printing_layout == 'action_print_check_voucher':
                    return self.env.ref('l10n_gt_check_printing.action_print_check_voucher').report_action(self)
                else:
                    return self.env.ref('l10n_gt_check_printing.action_print_check_format').report_action(self)
                #return self.env.ref('l10n_gt_check_printing.%s' % check_layout).report_action(self) #este es el external id del reporte.
        return super(account_payment, self).do_print_checks()
