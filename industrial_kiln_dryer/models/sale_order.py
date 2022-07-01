from odoo import api, fields, models

class SaleOrder(models.Model):
  _inherit = 'sale.order'

  job_number = fields.Text(string="Job Number", readonly=True)
  prefix = fields.Selection([
      ('j01', 'J01'), 
      ('j02', 'J02'), 
      ('j03', 'J03'), 
      ('j04', 'J04')
    ],
    string='Prefix',
    required=True
  )
  
  sufix = fields.Selection([
      ('01', '01'), 
      ('02', '02'), 
      ('03', '03'), 
      ('04', '04')
    ],
    tring='sufix',
    required=True
  )

  @api.model
  def create(self, vals):
    vals['job_number'] = self.env['ir.sequence'].next_by_code(vals['prefix'] + vals['sufix'])
    if not vals['job_number']:
      vals['job_number'] = self.env['ir.sequence'].create({
        'name': 'Job Number',
        'code': vals['prefix'] + vals['sufix'],
        'prefix': vals['prefix'],
        'suffix': vals['sufix'],
        'padding': 5,
        'number_next': 13500,
        'number_increment': 1,
        'implementation': 'standard',
      }).next_by_code(vals['prefix'] + vals['sufix'])
    return super().create(vals)

  
  def action_confirm(self):
    res = super().action_confirm()
    if not self.partner_id.has_sale_order_confirmed:
      self.partner_id.create_plant_prefix()
      self.partner_id.has_sale_order_confirmed = True
    return res
