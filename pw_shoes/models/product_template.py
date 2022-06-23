# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit="product.template"

    """
    Requirement 1 -  Adding new field that will be used in the price calculation
    Pair per Case - This field will be used to enter an integer which is the number of pair of shoes in the case
    Price per Pair - This field will be used to enter the price per pair. It can be a monetary field. 
    """

    pair_per_case = fields.Integer(string="Pair per Case")

    price_per_pair = fields.Monetary(string="Price per Pair")

    list_price = fields.Float(compute="_compute_sales_price",store=True)

    """
    Sales Price - This field uses the pair per case and price per pair to calculate the Sales price (Pair per price X Price per Pair).
    If nothing is entered in the Pair per Case and Price per Pair, the Sales price should be editable.
    If something is entered in Pair per Price or Price per Pair, the field should be read-only.
    """



    @api.depends("pair_per_case","price_per_pair")
    def _compute_sales_price(self):
        for record in self:
            _logger.info("************************* Executing compute_sales_price")
            if self.pair_per_case or self.price_per_pair:
                _logger.info("************************* Pair per case: " + str(self.pair_per_case) + " * Price per pair: " + str(self.price_per_pair))
                self.list_price = self.pair_per_case * self.price_per_pair
                _logger.info("************************* = " + str(self.list_price))