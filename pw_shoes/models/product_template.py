# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit="product.template"

    """
    Requirement 1 -  Adding new field that will be used in the price calculation
    Pair per Case - This field will be used to enter an integer which is the number of pair of shoes in the case
    Price per Pair - This field will be used to enter the price per pair. It can be a monetary field. 
    """

    pair_per_case = fields.Integer(string="Pair per Case")

    price_per_pair = fields.Monetary(string="Price per Pair")