# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
from odoo.tools import config


class Partner(models.Model):
    _inherit = 'res.partner'

    team_id = fields.Many2one("crm.team","Equipo de Ventas")
    legal_name = fields.Char("Razon Social")
    vat = fields.Char("NIT")

    @api.constrains('vat')
    def _check_vat_unique(self):
        for record in self:
            if record.parent_id or not record.vat:
                continue
            test_condition = (config['test_enable'] and
                              not self.env.context.get('test_vat'))
            if test_condition:
                continue
            results = self.env['res.partner'].search_count([
                ('parent_id', '=', False),
                ('vat', '=', record.vat),
                ('id', '!=', record.id)
            ])
            if results:
                raise ValidationError(_(
                    "The VAT %s already exists in another "
                    "partner.") % record.vat)

    _sql_constraints = [
        ('partner_legal_name_unique',
         'UNIQUE (country_id, legal_name)',
         '¡La razón social debe ser única por país!')]
