# -*- coding: utf-8 -*-
{
    'name': "td_generico_gt",

    'summary': """
        Tropicalización de 3Digital para Guatemala.""",

    'description': """
        Tipos de Documento
        Impuestos
        Datos fiscales en facturas
        Posiciones Fiscales
    """,

    'author': "3Digital",
    'website': "http://www.3digital.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'accounting',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/account_move_view.xml',
        'views/views.xml',
        'views/td_generico_invoice_view.xml',
        'views/invoice_cancel_view.xml',
        'views/report_invoice.xml',
      ],

}