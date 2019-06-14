# -*- coding: utf-8 -*-

from odoo import models, api, fields


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

    @api.multi
    def do_print_checks(self):
        self.cheque_formate_id = self._get_check_formate()
        if self:
            if self.journal_id.account_check_printing_layout != 'disabled':
                check_layout = self.journal_id.account_check_printing_layout
            else:
                check_layout = self[0].company_id.account_check_printing_layout
            if check_layout != 'disabled' and self[0].journal_id.company_id.country_id.code == 'GT':
                self.write({'state': 'sent'})
                return self.env.ref('l10n_gt_check_printing.action_report_print_cheque').report_action(self)  # este es el external id del reporte.
                #return self.env.ref('l10n_gt_check_printing.%s' % check_layout).report_action(self) #este es el external id del reporte.
        return super(account_payment, self).do_print_checks()
