from odoo import api,fields, models


class ProductTemplate(models.Model):
  _inherit = 'product.template'

  product_gender = fields.Selection([
        ('red', 'Red'),
        ('black', 'Black'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('green', 'Green')
    ], required=True, default='red')

  upc = fields.Many2one('ir.sequence', compute='_compute_upc')

  barcode = fields.Char(compute='_compute_barcode', store=True)

  @api.model
  def create(self, values):
    if isinstance(values, list):
      for value in values:
        self._assign_name(value)
    else:
      self._assign_name(values)
    return super().create(values)

  @api.model
  def _assign_name(self, value: dict):
    if not value.get('name') and value.get('categ_id'):
      value['name'] = self.env['ir.sequence'].browse(value['categ_id']).next_by_id()

  @api.depends('product_gender')
  def _compute_upc(self):
    for record in self:
      prefix = record.product_gender[:3].upper()
      seq = self.env['ir.sequence'].search([('code', '=', prefix)])
      if not seq:
        seq = self.env['ir.sequence'].create({
              'code': prefix,
              'name': record.product_gender,
              'prefix': prefix,
              'padding': 3
      })
      record.upc = seq

  @api.depends('upc')
  def _compute_barcode(self):
    for record in self:
      if record.upc:
        record.barcode = record.upc.next_by_id()
        