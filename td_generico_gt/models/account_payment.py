# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
from odoo.tools import config

class account_payment_ref(models.Model):
    _inherit = "account.payment"

    reference = fields.Char("Referencia")

    type = fields.Selection(
            [
            ("E", "Efectivo"),
            ("C", "Cheque"),
            ("T", "Transferencia"),
            ("TC", "Tarjeta de Credito"),
            ("DE", "Deposito"),
        ],
        string="Forma de Pago"
    )
    reference = fields.Char("Referencia")