from odoo import models

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"
  
  def confirm_rfqs(self):
    odoobot = self.env.ref('base.partner_root')
    partner = self.env['res.partner'].search([('name', '=', 'Mindesa SAPI de CV')])
    orders  = self.env['purchase.order'].search([
      ('user_id.id','=',odoobot.id),
      ('partner_id.id','=',partner.id)
    ])
    orders.button_confirm()
    
