# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID


class sale_order(models.Model):
    _inherit = "sale.order"

    @api.depends('user_id')
    def _get_group_comercial(self):
        for obj in self:
            bandera = False
            if obj.user_id:
                if obj.user_id.has_group("BBCV.group_BBCV_Comercial_jefe"):
                    bandera = True
            obj.is_comercial = bandera


# 	def _get_default_comercial(self, cr, uid, context=None):
# 		bandera = self.pool.get('res.users').has_group(cr, uid, "BBCV.group_BBCV_Comercial_jefe")
# 		return bandera


    @api.depends('user_id')
    def _get_group_pricing(self):
        for obj in self:
            bandera = False
            if obj.user_id:
                if obj.user_id.has_group("BBCV.group_BBCV_Pricing"):
                    bandera = True
            obj.is_pricing = bandera
# 
# 	def _get_default_pricing(self, cr, uid, context=None):
# 		bandera = self.pool.get('res.users').has_group(cr, uid, "BBCV.group_BBCV_Pricing")
# 		return bandera
    is_comercial = fields.Boolean(compute='_get_group_comercial', string="Comercial")
    is_pricing = fields.Boolean(compute='_get_group_pricing', string="Pricing")

# 	_defaults = {
# 		'is_comercial': _get_default_comercial,
# 		'is_pricing': _get_default_pricing,
# 	}
