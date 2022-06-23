# *-* coding: utf-8 *-*
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pair_p_case = fields.Integer(
        string='Pair Per Case', readonly=False, default=None)
    price_p_pair = fields.Monetary(string='Price per pair', default=None)

    list_price = fields.Float(string="Sales Price", states={'editable': [('readonly', False)], 'read_only': [
                              ('readonly', True)]}, compute='_calculate_sale_price', store=True)
    state = fields.Selection([('editable', 'Editable'), ('read_only', 'Read Only')],
                             'Status', copy=False, default='editable', invisible=True)

    @api.depends('pair_p_case', 'price_p_pair')
    def _calculate_sale_price(self):
        self.state = 'editable'
        for record in self.filtered(lambda r: (r.pair_p_case and r.price_p_pair)):
            record.list_price = record.pair_p_case * record.price_p_pair
            record.state = 'read_only'
