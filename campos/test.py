# -*- coding: utf-8 -*-

import time
from openerp.tools.translate import _
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp


class sale_order_new(osv.osv):
    _inherit = "sale.order"



    def _amount_all_pricing(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                'profit_pricingg': 0.0,
                'profit_finall': 0.0,
                'utilidad': 0.0,
                'utilidad2': 0.0,
            }
            val3 = val2 = val1 = 0.0
            cur = order.pricelist_id.currency_id
            for line in order.order_line:
                val2 += line.profit_final
                val3 += line.precio_venta
                val1 += line.profit_pricing  
            res[order.id]['profit_pricingg'] = cur_obj.round(cr, uid, cur, val1)
            res[order.id]['profit_finall'] = cur_obj.round(cr, uid, cur, val2)
            res[order.id]['utilidad'] = 0.00
            if res[order.id]['profit_finall'] > 0.00:
               res[order.id]['utilidad'] = (res[order.id]['profit_pricingg'] / val3) * 100.00
               res[order.id]['utilidad2'] = (res[order.id]['profit_finall'] / val3) * 100.00
            if res[order.id]['profit_finall'] <= 0.00:
               res[order.id]['utilidad'] = 0.00
               res[order.id]['utilidad2'] = 0.00

        return res
       
    def _get_order(self, cr, uid, ids, context=None):
        result = {}
        for line in self.pool.get('sale.order.line').browse(cr, uid, ids, context=context):
            result[line.order_id.id] = True
        return result.keys()
            
    _columns = {
        'direccion_origen': fields.char('Direccion origen', write=['BBCV.group_pricing_bbc']),
        'direccion_destino':fields.char('Direccion destino', write=['BBCV.group_pricing_bbc']),
        'puerto_orig':      fields.many2one('res.country.puerto','Puerto de origen', write=['BBCV.group_comercial_bbc']),
        'aero_orig':        fields.many2one('res.country.aereo','Aeropuerto de origen', write=['BBCV.group_comercial_bbc']),
        'frontera_orig':    fields.many2one('res.country.frontera','Frontera de origen', write=['BBCV.group_comercial_bbc']),
        'direc_destino':fields.char('Direccion de destino', write=['BBCV.group_comercial_bbc']),
        'puerto_dest':fields.many2one('res.country.puerto','Puerto de destino', write=['BBCV.group_comercial_bbc']),
        'aero_destino':fields.many2one('res.country.aereo','Aeropuerto de destino', write=['BBCV.group_comercial_bbc']),
        'front_destino':fields.many2one('res.country.frontera','Frontera de destino', write=['BBCV.group_comercial_bbc']),
        'cant_contenedores':fields.char('Cantidad de contenedores', write=['BBCV.group_comercial_bbc']),
        'observaciones1':fields.text('Observaciones'),
        'so_subtitulos2':fields.char(''),
        'pais_origen': fields.many2one('res.country', 'Pais Origen', write=['BBCV.group_comercial_bbc']),
        'pais_destino': fields.many2one('res.country', 'Pais Destino', write=['BBCV.group_comercial_bbc']),
        'profit_pricingg': fields.function(_amount_all_pricing, digits_compute=dp.get_precision('Account'), string='Profit Pricing',
            multi='sums', help="The total pricing."),
        #'profit_pricingg': fields.float('Profit Pricing', digits=(16,2)),
        'profit_finall': fields.function(_amount_all_pricing, digits_compute=dp.get_precision('Account'), string='Profit Final',
            multi='sums', help="The total profit final."),
        'utilidad': fields.function(_amount_all_pricing, digits_compute=dp.get_precision('Account'), string='% de utilidad',
            multi='sums', help="% de utilidad."),
        'utilidad2': fields.function(_amount_all_pricing, digits_compute=dp.get_precision('Account'), string='% de utilidad comercial',
            multi='sums', help="% de utilidad2."),
        'puerto_carga':    fields.many2one('res.country.puerto', 'Puerto de carga (POL)', write=['BBCV.group_pricing_bbc']),
        'puerto_descarga': fields.many2one('res.country.puerto', 'Puerto de descarga (POD)', write=['BBCV.group_pricing_bbc']),
        'aereo_origen' :   fields.many2one('res.country.aereo', 'Aereopuerto de origen', write=['BBCV.group_pricing_bbc']),
        'aereo_destino' :  fields.many2one('res.country.aereo', 'Aereopuerto de destino', write=['BBCV.group_pricing_bbc']),
        'frontera_origen': fields.many2one('res.country.frontera', 'Frontera de origen', write=['BBCV.group_pricing_bbc']),
        'frontera_destino':fields.many2one('res.country.frontera', 'Frontera de destino', write=['BBCV.group_pricing_bbc']),
  
    }
    

    def pais_onchange(self,cr,uid,ids, pais_origen):
        product_obj = self.pool.get('res.country.puerto')
        product_ids = product_obj.search(cr,uid, [('country_id','=',pais_origen)])
        product_obj2 = self.pool.get('res.country.frontera')
        product_ids2 = product_obj2.search(cr,uid, [('country_id','=',pais_origen)])
        product_obj3 = self.pool.get('res.country.aereo')
        product_ids3 = product_obj3.search(cr,uid, [('country_id','=',pais_origen)])
        return {'domain':{'puerto_carga':[('id','in',product_ids)], 'frontera_origen':[('id','in',product_ids2)], 'aereo_origen':[('id','in',product_ids3)]}}
        
    def pais_onchange_des(self,cr,uid,ids, pais_destino):
        product_obj = self.pool.get('res.country.puerto')
        product_ids = product_obj.search(cr,uid, [('country_id','=',pais_destino)])
        product_obj2 = self.pool.get('res.country.frontera')
        product_ids2 = product_obj2.search(cr,uid, [('country_id','=',pais_destino)])
        product_obj3 = self.pool.get('res.country.aereo')
        product_ids3 = product_obj3.search(cr,uid, [('country_id','=',pais_destino)])
        return {'domain':{'puerto_descarga':[('id','in',product_ids)], 'frontera_destino':[('id','in',product_ids2)], 'aereo_destino':[('id','in',product_ids3)]}}
        
sale_order_new()


class sale_order_line_new(osv.osv):
    _inherit = "sale.order.line"
	
	
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        res = super(sale_order_line_new, self).product_id_change(cr, uid, ids, pricelist, product, qty=qty,
            uom=uom, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)
        if not pricelist:
            return res
        frm_cur = self.pool.get('res.users').browse(cr, uid, uid).company_id.currency_id.id
        to_cur = self.pool.get('product.pricelist').browse(cr, uid, [pricelist])[0].currency_id.id
        if product:
            price_cost = self.pool.get('product.product').browse(cr, uid, product).standard_price
            price = self.pool.get('res.currency').compute(cr, uid, frm_cur, to_cur, price_cost, round=False)
            res['value'].update({'price_cost': price})
        return res
        
    def _amount_line_new(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        if context is None:
            context = {} 
        for line in self.browse(cr, uid, ids, context=context):
            cs = line.product_id.standard_price
            price = cs * line.product_uom_qty
            res[line.id] = price
                 
        return res
        
    def _amount_line_venta(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        abc=0
        if context is None:
            context = {} 
        for line in self.browse(cr, uid, ids, context=context):
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cur = line.order_id.pricelist_id.currency_id
            cc = cur_obj.round(cr, uid, cur, price_sale)
            res[line.id] = cc
            
            abc = line.price_cost
            state = line.profit_state
            if state == False:
               cs = line.product_id.standard_price or 0.0 
               price = cs * line.product_uom_qty or 1.00
               abc = price
               self.write(cr, uid, [line.id], {'profit_state': True})
            self.write(cr, uid, [line.id], {'price_cost': abc})
                        
        return res
        
    def _amount_line_pricing(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        if context is None:
            context = {} 
        for line in self.browse(cr, uid, ids, context=context):
            cs = line.product_id.standard_price
            price_cost = line.price_cost#cs * line.product_uom_qty
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cur = line.order_id.pricelist_id.currency_id
            cc = cur_obj.round(cr, uid, cur, price_sale)
            res[line.id] = cc - price_cost
        return res
        
    def _amount_line_final(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        if context is None:
            context = {} 
        for line in self.browse(cr, uid, ids, context=context):
            price_sale = (line.price_unit * (1 - (line.discount or 0.0) / 100.0) * line.product_uom_qty)
            cur = line.order_id.pricelist_id.currency_id
            cc = cur_obj.round(cr, uid, cur, price_sale)
            #res[line.id] = cc
            #if line.cost_operaciones <= cc:
            res[line.id] = cc - line.cost_operaciones
            
        return res
            
            
    _columns = {
        'proveedor': fields.many2one('res.partner', 'Proveedor',  states={'confirmed':[('readonly',True)], 'approved':[('readonly',True)],'done':[('readonly',True)]}, change_default=True, track_visibility='always'),
        #'price_cost': fields.function(_amount_line_new, string='Costo Pricing', digits_compute= dp.get_precision('Account')),
        'price_cost': fields.float('Costo Pricing', digits=(16,2)),
        'cost_operaciones': fields.float('Costo Operaciones', digits=(16,2)),
        'precio_venta': fields.function(_amount_line_venta, string='Precio de Venta', digits_compute= dp.get_precision('Account')),
        'profit_pricing': fields.function(_amount_line_pricing, string='Profit Pricing', type='float',  readonly=False, digits_compute= dp.get_precision('Account')),
        #'profit_pricing': fields.float('Profit Pricing', digits=(16,2)),
        'profit_state': fields.boolean('profit state'),
        'profit_final': fields.function(_amount_line_final, string='Profit Final', digits_compute= dp.get_precision('Account')),
    }
    _defaults = {
                'profit_state': False,
    }    
    
    
	
sale_order_line_new()


class puerto(osv.osv):
    _description="Aereopuertos por Pais"
    _name = 'res.country.puerto'
    _columns = {
        'country_id': fields.many2one('res.country', 'Pais',
            required=True),
        'name': fields.char('Nombre del Puerto ', size=64, required=True),
        'code': fields.char('Codigo del puerto', size=3,
            help='codigo.', required=True),
    }
    _order = 'code'

puerto()

class frontera(osv.osv):
    _description="Fronteras por Pais"
    _name = 'res.country.frontera'
    _columns = {
        'country_id': fields.many2one('res.country', 'Pais',
            required=True),
        'name': fields.char('Nombre de la frontera ', size=64, required=True),
        'code': fields.char('Codigo de la frontera', size=3,
            help='codigo.', required=True),
    }
    _order = 'code'

frontera()


class aereopuerto(osv.osv):
    _description="Aereopuertos por Pais"
    _name = 'res.country.aereo'
    _columns = {
        'country_id': fields.many2one('res.country', 'Pais',
            required=True),
        'name': fields.char('Nombre del Aereopuerto ', size=64, required=True),
        'code': fields.char('Codigo del Aereopuerto', size=3,
            help='codigo.', required=True),
    }
    _order = 'code'

aereopuerto()


