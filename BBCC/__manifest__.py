# -*- coding: utf-8 -*-

{
    'name': 'BBCC',
    'version': '1.0',
    'category': 'Sales Management',
    #'sequence': 14,
    #'summary': 'Quotations, Sales Orders, Invoicing',
    'description': """
        Modulo Clientes.
    """,
    'author': 'WEN',
    'website': 'http://www.openerp.com',
    #'images': ['images/sale_dashboard.jpeg','images/Sale_order_line_to_invoice.jpeg','images/sale_order.jpeg','images/sales_analysis.jpeg'],
    'depends': ['base', 'product', 'crm', 'sale','purchase'],
    'data': [
        'views/BBCC_view.xml',
        'security/ir.model.access.csv',
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
