from odoo import api,fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  name = fields.Text(string='Product Name', readonly=True, default='New')
  _sql_constraints = [('name_uniq','unique(name)','The product name must be unique')]

  @api.model
  def create(self, vals):
    product_category = self.env['product.category'].search([('id','=',vals.get('categ_id'))])
    prefix = product_category.name + '/'
    gender = self._search_category_gender(product_category.id)
    sequence_code = 'sequence.{}'.format(product_category.name)
    if not self.env['ir.sequence'].search([('code', '=', sequence_code)]):
      self.env['ir.sequence'].create({
        'name': product_category.name,
        'code': sequence_code,
        'prefix': prefix,
        'padding': 4,
        'number_increment': 1,
        'number_next': 1,
        'implementation': 'standard',
      })
    vals['name'] = self.env['ir.sequence'].next_by_code(sequence_code)
    vals['barcode'] = self._generate_barcode_seq(product_category, gender)
    return super(ProductTemplate, self).create(vals)
  
  def _search_category_gender(self, category_id):
    return self.env['product.category'].search([('id','=', category_id)]).gender

  def _generate_barcode_seq(self, product_category, gender):
    sequence_code = 'gender_seq.{}'.format(gender)
    if not self.env['ir.sequence'].search([('code', '=', sequence_code)]):
      self.env['ir.sequence'].create({
        'name': gender,
        'code': sequence_code,
        'prefix': gender,
        'padding': 15,
        'number_increment': 1,
        'number_next': 1,
        'implementation': 'standard',
      })
    return self.env['ir.sequence'].next_by_code(sequence_code) 

