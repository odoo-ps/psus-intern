# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fgd_salesperson_pricelist_readonly = fields.Boolean('Salesperson and Pricelist Readonly',
                                                        required=True,
                                                        default=False)

    @api.model
    def create(self, values):
        orig = super().create(values)
        orig.write({'fgd_salesperson_pricelist_readonly': True})
        return orig
