# -*- coding: utf-8 -*-

{
    'name': 'BBCC',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """
        Modulo Clientes.
    """,
    'author': 'WEN',
    'website': 'http://www.openerp.com',
    'depends': ['base', 'product', 'crm', 'sale','purchase'],
    'data': [
        'views/BBCC_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
