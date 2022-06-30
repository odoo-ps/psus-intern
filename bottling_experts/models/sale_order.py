from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    opportunity_name=fields.Char(string='Opportunity Name')
    travel_in = fields.Datetime("Travel In",  store=True)
    travel_out = fields.Datetime("Travel Out",  store=True)

    
   
