from odoo import _, api, fields, models

class Purchase_Order(models.Model):
    _inherit = 'purchase.order' #inherit from purchase to get access to draft attribute

    @api.model
    def _get_orders_to_confirm(self): 

        return self.search([
            ('state', '=', 'draft'), #All RFQs that are not sent to purchase already
            ('partner_id.id', '=', '1'), #where the vendor is Mindesa
            ('user_id.id', '=', '1'), # and creator was OdooBot
        ])

    def _confirm_rfq(self): 
        orders = self._get_orders_to_confirm() #Get all the orders to purchase

        for order in orders: 
            order.state = 'purchase' #and change the state to purchase
