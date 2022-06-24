# -*- encoding: utf-8 -*-

from odoo import api,fields,models

class linkedSale(models.Model):
    _inherit = 'sale.order'

    customer_orders = fields.Many2one(comodel_name='res.partner', ondelete='cascade')
