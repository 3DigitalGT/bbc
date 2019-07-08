# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, _
from odoo.exceptions import ValidationError
from odoo.tools import config


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def _check_vat_unique(self):
        for record in self:
            if record.parent_id or not record.vat:
                continue
            test_condition = (config['test_enable'] and
                              not self.env.context.get('test_vat'))
            if test_condition:
                continue
            if self._validate_nit(record.vat):
                results = self.env['res.partner'].search_count([
                    ('parent_id', '=', False),
                    ('vat', '=', record.vat),
                    ('id', '!=', record.id)
                ])
                if results:
                    raise ValidationError("El número de NIT ya existe. Por favor revisar.")
            else:
                raise ValidationError("Número de NIT Inválido. Por favor revisar.")

    def _validate_nit(self,nit):
        if nit == 'C/F':
            return True
        nit = nit.replace('-','')
        lado_izq = nit[:-1]
        lado_der = nit[-1:]
        if (lado_der.upper() == 'K'):
            verificador = 10
        else:
            try:
                int(lado_der)
            except ValueError:
                return False
            verificador = int(lado_der)
        try:
            int(lado_izq)
        except ValueError:
            return False
        sumatoria = 0
        largo = len(lado_izq)
        for x in range(1,largo+1):
            sumatoria += int(lado_izq[largo-x])*(x+1)
        dig1 = sumatoria - ((sumatoria // 11) * 11)
        dig2 = dig1 - ((dig1 // 11) * 11)
        digito_verificador = 11 - dig2
        if verificador == digito_verificador:
            return lado_izq + lado_der
        else:
            return False

    def _strip_dash(self,nit):
        return nit.replace('-','')