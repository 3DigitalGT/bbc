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
    'name': 'BBCV',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """ Este es el modulo de PRESUPUESTOS y PEDIDOS DE VENTA MODIFICADOS """,
    'author': 'Josepablo',
    'website': 'www.corpindustriasca.com',
    'depends': ['base', 'product', 'crm', 'sale_crm'],
    'data': [
        'security/ir.model.access.csv',
        'security/bbc_groups.xml',
        'views/bbcv_account_invoice_view.xml',
        'views/BBCV_view.xml',
        'views/test_view.xml',
        'views/BBCV_container_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
