# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID


class bbc_compras(models.Model):
    _inherit = "purchase.order"

    po_tipo_servicios = fields.Many2one('po_tipo_servicio','Tipo de servicio',ondelete='cascade',select=True)
    po_ref_pedido = fields.Many2one('sale.order','Referencia de pedido')
    po_responsable = fields.Many2one('res.partner','Responsable')
    po_plazo_pago = fields.Date('Plazo de pago')
    po_inicio_servicio = fields.Date('Fecha inicio servicio')
    po_fin_servicio = fields.Date('Fecha fin servicio')
    po_motivos_cancelar = fields.Many2one('po_motivo_cancelar','Motivo de cancelacion',ondelete='cascade',select=True)
    po_observaciones = fields.Char('Observaciones')


class po_tipo_servicio(models.Model):
    _name = 'po_tipo_servicio'
    _description = 'Tipo de servicio'

    name = fields.Char('Descripcion')


class po_motivo_cancelar(models.Model):
    _name = 'po_motivo_cancelar'
    _description = 'Motivo de cancelacion'

    name = fields.Char('Descripcion')

