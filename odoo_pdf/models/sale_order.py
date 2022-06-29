# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    opportunity_name = fields.Char(string='Opportunity Name')

    travel_in = fields.Date(string='Travel In')
    travel_out = fields.Date(string='Travel Out')

    @api.onchange('travel_in', 'travel_out')
    def onchange_travel_in_out(self):
        #validate that travel_in is before travel_out
        if self.travel_in and self.travel_out:
            if self.travel_in > self.travel_out:
                raise ValidationError(_('Travel In date must be before Travel Out date'))
