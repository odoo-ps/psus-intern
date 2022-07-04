import re
from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    plant_code = fields.Char(
      string='Plant Code',
      compute='_compute_plant_code'
    )
    plant_prefix = fields.Char(string='Plant prefix')

    has_sale_order_confirmed = fields.Boolean(string='Sale order confirmed?')

    @api.depends('has_sale_order_confirmed')
    def _compute_plant_code(self):
      for partner in self:
        if partner.has_sale_order_confirmed and not partner.plant_code:
          sequence = self.env['ir.sequence'].create({
            'name': 'Plant Code',
            'code': partner.plant_prefix,
            'prefix': partner.plant_prefix,
            'padding': 5,
            'implementation': 'standard',
            'number_next': 101,
            "number_increment": 1,
            "active": True,
          }).next_by_code(partner.plant_prefix)
          sequence = str(sequence)
          partner.plant_code = sequence[0:6] + '-' + sequence[6:]
        else:
          partner.plant_code = False

    def create_plant_prefix(self):
        if self.is_company:
            name = self.name
        else:
            name = self.parent_id.name if self.parent_id else self.name
        name = re.sub('[^A-Za-z0-9]+', '', name)
        self.plant_prefix = name.upper()[0:3] if len(name) >= 3 else name
