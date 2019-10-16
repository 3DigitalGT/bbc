# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID

class sale_order(models.Model):
    _inherit = "sale.order"

    container_ids = fields.One2many("sale.container","saleorder_id","Contenedores")
    electricity_bbc = fields.Boolean("Energía Electrica")
    electricity_nav = fields.Boolean("Energía Electrica")
    forwarding_agent = fields.Many2one("res.partner","Forwarding Agent")
    documents_to = fields.Many2one("res.partner", "Present Documents to")
    precarriage_by =  fields.Many2one("res.partner", "Precarriage By")
    precarriage_location = fields.Char("Place Receipt be Precarriage")
    routing = fields.Char("Routing")
    booking = fields.Char("Booking")
    export_references = fields.Char("Export References")
    type_of_move = fields.Char("Tipo de Movimiento")

class res_partner_container(models.Model):
    _inherit = "res.partner"

    saleorder_notify_ids = fields.One2many("sale.order","so_notify_id","Notify")

class sale_container(models.Model):
    _name = 'sale.container'

    type = fields.Selection([
        ('40', '40 Pies'),
        ('20', '20 Pies'),
        ('40H', '40 Pies Hi'),
    ])
    saleorder_id = fields.Many2one('sale.order',"SO")
    number = fields.Char('Number', required = True)
    seal = fields.Char('Marchamo', required = True)
    pieces = fields.Integer('Piezas', required=True )
    marks = fields.Char("Marcas")
    weight_net = fields.Integer("Peso Neto")
    weight_exp = fields.Integer("Peso Esperado (Kg)")
    exp_volume = fields.Integer("Volumen Esperado (CBM)")
    package_ids = fields.One2many('sale.container.pkg','container_id',"Paquetes")
    weight_total = fields.Integer("Peso Total", compute = "get_total_weight", store = True)

    def get_total_weight(self):
        self.weight_total = 0

class sale_container_pkg(models.Model):
    _name = 'sale.container.pkg'

    container_id = fields.Many2one("sale.container","Contenedor")
    qty = fields.Integer("Cantidad",required = True)
    wrap_id = fields.Many2one('sale.container.wrap',string = "Empaque")
    description =  fields.Char('Descripción', required = True)
    weight = fields.Integer("Peso", required = True)
    volume = fields.Integer("Volumen", required = True)

class sale_container_wrap(models.Model):
    _name = "sale.container.wrap"

    name = fields.Char("Nombre")
    container_pkg_ids = fields.One2many("sale.container.pkg","wrap_id","Paquetes")
