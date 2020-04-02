# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Campos nuevos Sale Orders',
    'version': '1.0',
    'category': 'Sales Management',
    #'sequence': 14,
    #'summary': 'Quotations, Sales Orders, Invoicing',
    'description': """
Campos nuevos...........""",
    'author': 'Corp Industriasl',
    'website': 'http://www.openerp.com',
    #'images': ['images/sale_dashboard.jpeg','images/Sale_order_line_to_invoice.jpeg','images/sale_order.jpeg','images/sales_analysis.jpeg'],
    'depends': ['base', 'sale', 'BBCV'],
    'data': [
        'security/ir.model.access.csv',
        'views/test_view.xml',
    ],
    #'demo': ['sale_demo.xml'],
    #'test': [
    #    'test/sale_order_demo.yml',
    #    'test/manual_order_policy.yml',
    #    'test/cancel_order.yml',
    #    'test/delete_order.yml',
    #    'test/edi_sale_order.yml',
    #],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
