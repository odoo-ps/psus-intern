from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    plant_no = fields.Char(string='Plant Number',
                           readonly=True)
