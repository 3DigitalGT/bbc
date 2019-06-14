# -*- coding: utf-8 -*-

from openerp import models, api, fields

class res_company(models.Model):
    _inherit = "res.company"

    account_check_printing_layout = fields.Selection(string="Formato Cheque", required=True,
        help="Seleccione el formato que desea utilizar para imprimir sus cheques.\n"
             "Para deshabilitar la función, seleccione 'Ninguno'.",
        selection=[
            ('disabled', 'Ninguno'),
            ('action_print_check_voucher', 'Voucher'),
            ('action_print_check_format', 'Formato'),
        ],
        default="action_print_check_format")