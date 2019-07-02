# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    legal_name = fields.Char("Razon Social")


class AccountTax(models.Model):
    _inherit = "account.tax"
    is_vat = fields.Boolean("Es IVA")


class Invoice(models.Model):
    _inherit = "account.invoice"
    doc_serie = fields.Char("Serie Factura")
    doc_type = fields.Selection(selection=[("ONAF","ONAF"),("FCE","FCE"),("FC","FC"),("FPC","FPC")],string="Tipo Documento")
    doc_number = fields.Char("Numero Factura")

    _sql_constraints = [
        ('partner_serie_numero_unique',
         'UNIQUE (partner_id, doc_serie, doc_number)',
         'La Serie y Número de documento debe ser unica por proveedor!')]

class account_payment_ref(models.Model):
    _inherit = "account.payment"

    type = fields.Selection(
        [
            ("E","Efectivo"),
            ("C","Cheque"),
            ("T","Transferencia"),
            ("TC","Tarjeta de Credito"),
        ],
        string = "Forma de Pago"
    )
    reference = fields.Char("Referencia")