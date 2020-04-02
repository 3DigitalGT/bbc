# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
import calendar
from calendar import monthrange
import datetime

class report_purchase_sale_ledger_report_so_po_ledger(models.AbstractModel):
    _name = 'report.purchase_sale_ledger.report_so_po_ledger'
    _description = 'Sale and Purchase ledger Report'

    def _get_invocie_id(self, year, month, report_title):
        days = monthrange(year, month)
        start_date = datetime.datetime(year, month, 1).date()
        end_date = datetime.datetime(year, month, days[1]).date()
        if report_title == 'Libro Compras':
            inv = self.env['account.invoice'].search([('type','in',['in_invoice','in_refund']),('date_invoice','>=',start_date),
                                                ('date_invoice','<=',end_date)])
            invoice_id = self.env['account.invoice'].search([('type','in',['in_invoice','in_refund']),
                                                ('date_invoice','>=',start_date),
                                                ('date_invoice','<=',end_date)])
            return invoice_id.sorted(key=lambda r: r.date_invoice) #todo: order by date, doc_serie, doc_number
        else:
            invoice_id = self.env['account.invoice'].search([('type','in',['out_invoice','out_refund']),
                                                ('date_invoice','>=',start_date),
                                                ('date_invoice','<=',end_date)])
            return invoice_id.sorted(key=lambda r: r.date_invoice) #todo: order by date, doc_serie, doc_number

    def _get_tax_calculat(self, invoice_ids):
        sub_total_good = sub_total_service = sub_total_idp = sub_total_nvat = sub_total_other = sub_total_vat = sub_total_import_export = sub_total_exempt = 0.0
        goods_untax_total = service_untax_total =tax_amount_goods = tax_amount_service = untax_nvat = untax_import_export =0.0
        tax_amount_nvat = tax_amount_imp_exp = tax_amount_idp = 0.0
        nvat_tax_amount_subtotal_upper = 0.0
        final_tax_dict = {}
        total_inv = 0
        # movelines.sorted(key=lambda r: r.date)
        for inv in invoice_ids:
            vat_tax_list ,other_tax_list , other_tax_amount_list , service_tax_list , imp_exp_list , good_tax_list =[],[],[],[],[],[]
            idp_tax_list , nvat_tax_list = [],[]
            goods_amount_total = import_export_tax= service_amount_total = idp_amount_total = nvat_amount_total = exempt_amount_total =vat_amount_total = other_amount_total = idp_tax_val = 0.0
            vat_tax_amount = other_total = nvat_tax_amount_upper = 0.0
            for inv_line in inv.invoice_line_ids:
                if inv_line.invoice_line_tax_ids:
                    if inv_line.product_id.type in ('consu','product'):
                        #import export tax
                        imp_exp_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'dai').ids
                        if imp_exp_tax_id:
                            for imp_t in imp_exp_tax_id:
                                import_export_tax += inv_line.price_subtotal
                                sub_total_import_export += inv_line.price_subtotal
                                if imp_t not in imp_exp_list:
                                    imp_exp_tax = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == imp_t).amount
                                    tax_amount_imp_exp += imp_exp_tax
                                    imp_exp_list.append(imp_t)
                        #goods tax
                        goods_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type in ('vat','other')).ids
                        for g_tax in goods_tax_id:
                            if goods_tax_id:
                                goods_amount_total += inv_line.price_subtotal
                                sub_total_good += inv_line.price_subtotal
                                if g_tax not in good_tax_list:
                                    good_amount_tax = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == g_tax).amount
                                    tax_amount_goods += good_amount_tax
                                    good_tax_list.append(g_tax)
                    #if product in service
                    if inv_line.product_id.type == 'service':
                        service_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type in ('vat','other')).ids
                        if service_tax_id:
                            for ser_t in service_tax_id:
                                service_amount_total += inv_line.price_subtotal
                                sub_total_service += inv_line.price_subtotal
                                if ser_t not in service_tax_list:
                                    service_tax_amount = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == ser_t).amount
                                    # for tax in service_tax_id:
                                    tax_amount_service += service_tax_amount
                                    service_tax_list.append(ser_t)
                    #vat tax amount
                    idp_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'idp').ids
                    if idp_tax_id:
                        for idp_t in idp_tax_id:
                            idp_amount_total += inv_line.price_subtotal
                            sub_total_idp += inv_line.price_subtotal
                            if idp_t not in idp_tax_list:
                                idp_tax_total = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == idp_t).amount
                                idp_tax_val += idp_tax_total
                                tax_amount_idp += idp_tax_total
                                idp_tax_list.append(idp_t)
                    #nvat tax amount
                    nvat_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'nvat').ids
                    if nvat_tax_id:
                        for nvat_t in nvat_tax_id:
                            nvat_amount_total += inv_line.price_subtotal
                            sub_total_nvat += inv_line.price_subtotal
                            # for tax in nvat_tax_id:
                            if nvat_t not in nvat_tax_list:
                                nvat_total = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == nvat_t).amount
                                nvat_tax_amount_upper +=  nvat_total
                                nvat_tax_amount_subtotal_upper += nvat_total
                                tax_amount_nvat += nvat_total
                                nvat_tax_list.append(nvat_t)

                    #other taxes
                    # other_type_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type in ('idp','dai','other')).ids
                    # if other_type_tax_id:
                    #     for othr_tax in other_type_tax_id:
                    #         other_tax_amount = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == othr_tax).amount
                    #         if othr_tax not in other_tax_list:
                    #         # for tax in vat_type_tax_id:
                    #             other_amount_total += other_tax_amount
                    #             sub_total_other += other_tax_amount
                    #             other_tax_list.append(othr_tax)

                    #vat type tax sum
                    vat_type_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'vat').ids
                    if vat_type_tax_id:
                        for vat_t in vat_type_tax_id:
                            vat_tax_amount = inv.tax_line_ids.filtered(lambda t: t.tax_id.id == vat_t).amount
                            if vat_t not in vat_tax_list:
                                vat_amount_total += vat_tax_amount
                                sub_total_vat += vat_tax_amount
                                vat_tax_list.append(vat_t)
                else:
                    exempt_amount_total += inv_line.price_subtotal
                    sub_total_exempt += inv_line.price_subtotal
                    if inv_line.product_id.type in ('consu','product'):
                        goods_untax_total += inv_line.price_subtotal
                    else:
                        service_untax_total += inv_line.price_subtotal
                    untax_imp_exp_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'dai').ids
                    if untax_imp_exp_tax_id:
                        untax_import_export += inv_line.price_subtotal
                    untax_nvat_tax_id = inv_line.invoice_line_tax_ids.filtered(lambda t: t.group_type == 'nvat').ids
                    if untax_nvat_tax_id:
                        untax_nvat += inv_line.price_subtotal
            total_inv += 1
            #return to report all tax value
            final_tax_dict.update({inv:{'import_export':import_export_tax, 
                                        'goods':goods_amount_total, 
                                        'service_tax':service_amount_total,
                                        'idp_tax':idp_amount_total,
                                        'idp_tax_val':idp_tax_val,
                                        'nvat_tax':nvat_amount_total,
                                        'exempt_tax':exempt_amount_total,
                                        'other_tax':other_amount_total,
                                        'vat_tax': vat_amount_total,
                                        'nvat_tax_amount': nvat_tax_amount_upper},
                                        'sub_total_goods':sub_total_good,
                                        'sub_total_import_export':sub_total_import_export,
                                        'sub_total_service':sub_total_service,
                                        'sub_total_idp':sub_total_idp,
                                        'sub_total_nvat':sub_total_nvat,
                                        'sub_total_other':sub_total_other,
                                        'sub_total_vat':sub_total_vat,
                                        'sub_total_exempt':sub_total_exempt,
                                        'sub_total_nvat_tax_amount':nvat_tax_amount_subtotal_upper,
                                        'goods_untax_total':goods_untax_total,
                                        'service_untax_total':service_untax_total,
                                        'untax_nvat':untax_nvat,
                                        'untax_import_export':untax_import_export,
                                        'tax_amount_goods':tax_amount_goods,
                                        'tax_amount_service':tax_amount_service,
                                        'tax_amount_imp_exp':tax_amount_imp_exp,
                                        'tax_amount_nvat':tax_amount_nvat,
                                        'tax_amount_idp':tax_amount_idp,
                                        'total_inv':total_inv,
                                        })
        return final_tax_dict
                    
    @api.model
    def _get_report_values(self, docids, data=None):
        year = data['form']['year']
        month = data['form']['month']
        report_title = data['report_title']
        invoice_ids = self._get_invocie_id(year, month, report_title)
        get_tax_calculation = self._get_tax_calculat(invoice_ids)
        # get_import_export_title = self._get_import_export_header()
        if report_title == 'Libro Compras':
            import_export_title = 'EXP'
        else:
            import_export_title = 'IMP'
        first_page_numbr = data['form']['first_page_number']
        return {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': invoice_ids,
            'data': data,
            'company_id': self.env['res.company'].browse(
                data['form']['company_id'][0]),
            'tax_value' : get_tax_calculation,
            'import_export_title': import_export_title,
            'first_page_number':first_page_numbr
        }
