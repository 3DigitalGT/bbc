# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID
from odoo.addons import decimal_precision as dp

# TE VOY A BORRAR

class sale_order_new(models.Model):
    _inherit = "sale.order"

    @api.one
    @api.depends('pricelist_id', 'order_line', 'profit_finall')
    def _amount_all_pricing(self):
        for data in self:
            val3 = 0.0
            val2 = 0.0
            val1 = 0.0
            cur = data.pricelist_id.currency_id
            for line in data.order_line:
                val2 += line.profit_final
                val3 += line.precio_venta
                val1 += line.profit_pricing 
            data.profit_pricingg = cur.round(val1)
            data.profit_finall = cur.round(val2)
            if data.profit_finall > 0.00:
                data.utilidad = (data.profit_pricingg / val3) * 100.00
                data.utilidad2= (data.profit_finall / val3) * 100.00
            if data.profit_finall <= 0.00:
                data.utilidad = 0.00
                data.utilidad2 = 0.00

    def _get_order(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order_id.id] = True
        return result.keys()

    direccion_origen = fields.Char('Direccion origen', write=['BBCV.group_pricing_bbc'])
    direccion_destino = fields.Char('Direccion destino', write=['BBCV.group_pricing_bbc'])
    puerto_orig = fields.Many2one('res.country.puerto', 'Puerto de origen', write=['BBCV.group_comercial_bbc'])
    aero_orig = fields.Many2one('res.country.aereo', 'Aeropuerto de origen', write=['BBCV.group_comercial_bbc'])
    frontera_orig = fields.Many2one('res.country.frontera', 'Frontera de origen', write=['BBCV.group_comercial_bbc'])
    direc_destino = fields.Char('Direccion de destino', write=['BBCV.group_comercial_bbc'])
    puerto_dest = fields.Many2one('res.country.puerto', 'Puerto de destino', write=['BBCV.group_comercial_bbc'])
    aero_destino = fields.Many2one('res.country.aereo', 'Aeropuerto de destino', write=['BBCV.group_comercial_bbc'])
    front_destino = fields.Many2one('res.country.frontera', 'Frontera de destino', write=['BBCV.group_comercial_bbc'])
    cant_contenedores = fields.Char('Cantidad de contenedores', write=['BBCV.group_comercial_bbc'])
    observaciones1 = fields.Text('Observaciones')
    so_subtitulos2 = fields.Char('Subtitulos2')
    pais_origen = fields.Many2one('res.country', 'Pais Origen', write=['BBCV.group_comercial_bbc'])
    pais_destino = fields.Many2one('res.country', 'Pais Destino', write=['BBCV.group_comercial_bbc']) 
    profit_pricingg = fields.Float(compute='_amount_all_pricing', digits_compute=dp.get_precision('Account'), string='Profit Pricing',
        help="The total pricing.")
    profit_finall = fields.Float(compute='_amount_all_pricing', digits_compute=dp.get_precision('Account'), string='Profit Final',
        help="The total profit final.")
    utilidad = fields.Float(compute='_amount_all_pricing', digits_compute=dp.get_precision('Account'), string='% de utilidad',
        help="% de utilidad.")
    utilidad2 = fields.Float(compute='_amount_all_pricing', digits_compute=dp.get_precision('Account'), string='% de utilidad comercial',
        help="% de utilidad2.")
    puerto_carga = fields.Many2one('res.country.puerto', 'Puerto de carga (POL)', write=['BBCV.group_pricing_bbc'])
    puerto_descarga = fields.Many2one('res.country.puerto', 'Puerto de descarga (POD)', write=['BBCV.group_pricing_bbc']) 
    aereo_origen = fields.Many2one('res.country.aereo', 'Aereopuerto de origen', write=['BBCV.group_pricing_bbc'])
    aereo_destino = fields.Many2one('res.country.aereo', 'Aereopuerto de destino', write=['BBCV.group_pricing_bbc']) 
    frontera_origen = fields.Many2one('res.country.frontera', 'Frontera de origen', write=['BBCV.group_pricing_bbc'])
    frontera_destino = fields.Many2one('res.country.frontera', 'Frontera de destino', write=['BBCV.group_pricing_bbc'])

    @api.onchange('pais_origen')
    def onchange_pais_origen(self):
        if self.pais_origen:
            product_obj = self.env['res.country.puerto']
            product_ids = product_obj.search([('country_id', '=', self.pais_origen.id)])
            product_obj2 = self.env['res.country.frontera']
            product_ids2 = product_obj2.search( [('country_id', '=', self.pais_origen.id)])
            product_obj3 = self.env['res.country.aereo']
            product_ids3 = product_obj3.search( [('country_id', '=', self.pais_origen.id)])
            return {'domain':{'puerto_carga':[('id', 'in', product_ids)], 'frontera_origen':[('id', 'in', product_ids2)], 'aereo_origen':[('id', 'in', product_ids3)]}}

    @api.onchange('pais_destino')
    def onchange_pais_destino(self):
        if self.pais_destino:
            product_obj = self.env['res.country.puerto']
            product_ids = product_obj.search([('country_id', '=', self.pais_destino.id)])
            product_obj2 = self.env['res.country.frontera']
            product_ids2 = product_obj2.search([('country_id', '=', self.pais_destino.id)])
            product_obj3 = self.env['res.country.aereo']
            product_ids3 = product_obj3.search([('country_id', '=', self.pais_destino.id)])
            return {'domain':{'puerto_descarga':[('id', 'in', product_ids)], 'frontera_destino':[('id', 'in', product_ids2)], 'aereo_destino':[('id', 'in', product_ids3)]}}


class sale_order_line_new(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(sale_order_line_new, self).product_id_change()
        if not self.order_id.pricelist_id.id:
            return res
        frm_cur = self.env['res.users'].browse(self._uid).company_id.currency_id
        to_cur = self.order_id.pricelist_id.currency_id
        if self.product_id:
            price_cost = self.product_id.standard_price
            price = self.env['res.currency']._compute(frm_cur, to_cur, price_cost, round=False)
            self.price_cost = price
        return res

    @api.one
    @api.depends('product_id', 'discount', 'product_uom_qty', 'order_id.pricelist_id')
    def _amount_line_venta(self):
        for line in self:
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cc = line.order_id.pricelist_id.currency_id.round(price_sale)
            line.precio_venta = cc
            abc = line.price_cost
            state = line.profit_state
            if state == False:
                cs = line.product_id.standard_price or 0.0 
                price = cs * line.product_uom_qty or 1.00
                abc = price
                line.profit_state = True
                line.price_cost = abc

    @api.one
    @api.depends('product_id', 'price_cost', 'discount', 'product_uom_qty', 'order_id.pricelist_id')
    def _amount_line_pricing(self):
        for line in self:
            price_cost = line.price_cost  # cs * line.product_uom_qty
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cc = line.order_id.pricelist_id.currency_id.round(price_sale)
            line.profit_pricing = cc - price_cost

    @api.one
    @api.depends('price_unit', 'discount', 'product_uom_qty', 'order_id.pricelist_id')
    def _amount_line_final(self):
        for line in self:
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cc = line.order_id.pricelist_id.currency_id.round(price_sale)
            line.profit_final = cc - line.cost_operaciones


    proveedor = fields.Many2one('res.partner', 'Proveedor', states={'confirmed':[('readonly', True)], 'approved':[('readonly', True)], 'done':[('readonly', True)]}, change_default=True, track_visibility='always')
    price_cost = fields.Float('Costo Pricing', digits=(16, 2))
    cost_operaciones = fields.Float('Costo Operaciones', digits=(16, 2))
    precio_venta = fields.Float(compute='_amount_line_venta', string='Precio de Venta', digits_compute=dp.get_precision('Account'))
    profit_pricing = fields.Float(compute='_amount_line_pricing', string='Profit Pricing', type='float', readonly=False, digits_compute=dp.get_precision('Account'))
    profit_state = fields.Boolean('profit state', default=False)
    profit_final = fields.Float(compute='_amount_line_final', string='Profit Final', digits_compute=dp.get_precision('Account'))


class puerto(models.Model):
    _description = "Aereopuertos por Pais"
    _name = 'res.country.puerto'
    _order = 'code'

    country_id = fields.Many2one('res.country', 'Pais',
        required=True)
    name = fields.Char('Nombre del Puerto ', size=64, required=True)
    code = fields.Char('Codigo del puerto', size=3,
        help='codigo.', required=True)


class frontera(models.Model):
    _description = "Fronteras por Pais"
    _name = 'res.country.frontera'
    _order = 'code'

    country_id = fields.Many2one('res.country', 'Pais',
        required=True)
    name = fields.Char('Nombre de la frontera ', size=64, required=True)
    code = fields.Char('Codigo de la frontera', size=3,
        help='codigo.', required=True)


class aereopuerto(models.Model):
    _description = "Aereopuertos por Pais"
    _name = 'res.country.aereo'
    _order = 'code'

    country_id = fields.Many2one('res.country', 'Pais',
        required=True)
    name = fields.Char('Nombre del Aereopuerto ', size=64, required=True)
    code = fields.Char('Codigo del Aereopuerto', size=3,
        help='codigo.', required=True)


