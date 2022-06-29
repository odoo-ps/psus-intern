from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    final_client = fields.Many2one(comodel_name='res.partner',
                                   string='Final client')
    opportunity_name = fields.Char(string='Opportunity name')
    travel_in = fields.Datetime(string='Travel in')
    travel_out = fields.Datetime(string='Travel out')

    @api.onchange('travel_in', 'travel_out')
    def onchange_travel_in_out(self):
        if self.travel_in and self.travel_out:
            if self.travel_out < self.travel_in:
                raise UserError(_('Travel out must be after travel in'))
