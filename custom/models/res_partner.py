# -*- coding:utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    product_list_ids = fields.Many2one(comodel_name='custom.productlists',
                                       string="Prooduct List"
                                      )
        