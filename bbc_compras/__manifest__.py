# -*- coding: utf-8 -*-

{
    'name': 'BBC compras',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """
Campos nuevos...........""",
    'author': 'WEN',
    'website': 'http://www.openerp.com',
    'depends': ['base', 'product', 'crm', 'sale', 'purchase'],
    'data': [
        'views/bbc_compras_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
