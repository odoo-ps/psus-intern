# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_studio_opportunity = fields.Char(string='Opportunity Name')

    travel_in_date = fields.Date(string='Travel In Date')

    travel_out_date = fields.Date(string='Travel Out Date')

    @api.constrains('travel_out_date')
    def _check_travel_out_date(self):
        for record in self:
            if record.travel_in_date and record.travel_out_date and record.travel_out_date < record.travel_in_date:
                raise ValidationError('Travel In Date must be smaller than or equal to Travel Out Date.')
