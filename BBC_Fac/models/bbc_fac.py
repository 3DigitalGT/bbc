# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID


class fac_test(models.Model):
    _inherit = 'account.invoice'

    xtipo_documento_cliente = fields.Many2one('xdocumento_cliente','Tipo de documento del cliente')
    tipo_documento_proveedor = fields.Many2one('documento_proveedor','Tipo de documento del proveedor')
    Referencia_en_Factura =  fields.Char('Referencia_en_ffactura', help='the email')
    Observaciones_d = fields.Text('Observaciones_d')
    Impresion_Consolidada_factgt =  fields.Boolean('Datos_Factura_Consolidada')
    Cantidad_taotal = fields.Integer('Facturacion_cantidad_Total',help='Total de la descripcion de factura')
    Descripcion_Unica_facturacion =  fields.Text('Facturacion_Unica_Guatemala')
    Unitario_fact = fields.Float('Facturacion_Unitario',digits=(30,2),help='precio unitario')
    Total_fact = fields.Float('Facturacion_Total',digits=(30,2),help='Total de la descripcion de factura')
    Impresion_Invoice =  fields.Boolean('Datos_Factura_Consolidada')
    Para_panama =  fields.Char('para_panama')
    Para_panamaPOD = fields.Char('para_panama')
    Para_panamaPOL = fields.Char('para_panama')


class documento_cliente(models.Model):
    _name = 'account.documento_cliente'
    _description = 'Tipo de documento del cliente'

    name = fields.Char('Descripcion', size=30)


class documento_proveedor(models.Model):
    _name = 'account.documento_proveedor'
    _description = 'Tipo de documento del proveedor'

    name = fields.Char('Descripcion', size=30)

