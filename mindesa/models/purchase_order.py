from odoo import _, api, fields, models

class Purchase_Order(models.Model):
    _inherit = 'purchase.order' 
            
    def _confirm_rfq(self):
        user_admin_id = self.env.ref('base.user_admin')
        odooBot_id = self.env.ref('base.user_root')
        for order in self.env['purchase.order'].search([('state', '=', 'draft'), ('user_id.id', '=', user_admin_id.id), ('partner_id.id', '=', odooBot_id.id)]):
            order.button_confirm()
