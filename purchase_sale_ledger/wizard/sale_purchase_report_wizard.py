# -*- coding: utf-8 -*-

from odoo import fields, models, api
import calendar
from calendar import monthrange
import datetime



class SalePurchaseLedgerWizard(models.TransientModel):
    _name = "sale.purchase.ledger.wiz"
    _description = "Sale Purchase Ledger Wizard"

    def get_years():
        year_list = []
        for i in range(2010, 2025):
            year_list.append((i, str(i)))
        return year_list

    ledger_type = fields.Selection([('purchase','Compras'),('sale','Ventas')],default='purchase')
    company_id = fields.Many2one('res.company',string="Company",default=lambda self: self.env.user.company_id)
    year = fields.Selection(get_years(), string='Year',default=datetime.datetime.now().year)
    month = fields.Selection([(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                          (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                          (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'), ],
                          string='Month',default=datetime.datetime.now().month)
    first_page_number=fields.Integer("Folio Inicial",default=1)

    # def _get_invocie_id(self):
    #     days = monthrange(self.year, self.month)
    #     start_date = datetime.datetime(self.year, self.month, 1).date()
    #     end_date = datetime.datetime(self.year, self.month, days[1]).date()
    #     if self.ledger_type == 'purchase':
    #         invoice_id = self.env['account.invoice'].search([('type','=','in_invoice'),
    #                                             ('date_invoice','>=',start_date),
    #                                             ('date_invoice','<=',end_date)])
    #         return invoice_id
           
    @api.multi
    def print_report(self):
        self.ensure_one()
        datas={}
        res = self.read(['company_id', 'year', 'month','first_page_number'])
        res = res and res[0] or {}
        # res['price_list'] = res['price_list'][0]
        datas['form'] = res
        if self.ledger_type == 'purchase':
            datas.update({'report_title':'Libro Compras'})
        else:
            datas.update({'report_title':'Libro Ventas'})
        if self.month:
            calendar.month_name[3]
            # mm = datetime.datetime.strptime(str(self.month), '%B').month
            datas.update({'mm':calendar.month_name[3]})
        if self.year:
            datas.update({'yyyy':self.year})
        # invoice_ids = self._get_invocie_id()
        # datas.update({'inv_ids':invoice_ids})


        return self.env.ref('purchase_sale_ledger.action_report_so_po_inv_ledger').with_context(landscape=True).report_action(self, data=datas)
