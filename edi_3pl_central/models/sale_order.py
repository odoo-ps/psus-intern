# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES


class Partner(models.Model):
    _inherit = 'res.partner'

    shipping_collect_account = fields.Char('Shipping Collect Account')
    warehouse_instructions = fields.Text('Warehouse Instructions')
    ship_priority = fields.Selection(PROCUREMENT_PRIORITIES, string='Priority', default='0')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    shipping_collect_account = fields.Char('Shipping Collect Account')
    warehouse_instructions = fields.Text('Warehouse Instructions')

    shipping_carrier = fields.Many2one(string="Shipping Carrier", comodel_name='delivery.carrier')
    shipping_billing_code = fields.Char(related="shipping_carrier.billing_code")
    ship_priority = fields.Selection(PROCUREMENT_PRIORITIES, string='Priority', default='0')

    @api.onchange('partner_id')
    def _onchange_partner_set_shipping(self):
        for order in self:
            order.shipping_collect_account = order.partner_id.shipping_collect_account
            order.warehouse_instructions = order.partner_id.warehouse_instructions
            order.ship_priority = order.partner_id.ship_priority