from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit="product.template"
    name = fields.Char(index=True, required=True, translate=True, default=lambda self: _('New'), readonly=True)   
    upc = fields.Char(string='UPC')
    _sql_constraints = [
        ('name_unique', 'unique (name)', "Product with the same name already exists."),
    ]
    @api.model
    def create(self, vals):
        product_category = self.env['product.category'].search([('id','=',vals.get('categ_id'))])
        if vals.get('name', _('New')) == _('New'):
            if not self.env['ir.sequence'].search([('code', '=', 'sequence.{}'.format(product_category.name))]):
                self.env['ir.sequence'].create({
                    'name': product_category.name,
                    'code': 'sequence.'+product_category.name,
                    'implementation': 'standard',
                    'prefix': product_category.name,
                    'padding': 4,
                    'number_increment': 1,
                    'number_next': 1,               
                })
            vals['name'] = self.env['ir.sequence'].next_by_code('sequence.'+str(product_category.name))
            vals['upc'] = self.barcode_generate(product_category)
            return super(ProductTemplate, self).create(vals)
    
    
 
    def write(self, vals):
        product_category = self.env['product.category'].search([('id','=',vals.get('categ_id'))])
        
        if not self.env['ir.sequence'].search([('code', '=', 'sequence.{}'.format(product_category.name))]):
                self.env['ir.sequence'].create({
                    'name': product_category.name,
                    'code': 'sequence.'+product_category.name,
                    'implementation': 'standard',
                    'prefix': product_category.name,
                    'padding': 4,
                    'number_increment': 1,
                    'number_next': 1,               
                })
        vals['name'] = self.env['ir.sequence'].next_by_code('sequence.'+str(product_category.name))
        return super(ProductTemplate, self).write(vals)

    def barcode_generate(self,product_category):
        
        barcode_sequence_name = product_category.name 
        prefix = product_category.gender+" "+str(product_category.id)      
        if not self.env['ir.sequence'].search([('code', '=', 'barcodesequence.'+ barcode_sequence_name)]):  
            self.env['ir.sequence'].create({
            'name': barcode_sequence_name,
            'code': 'barcodesequence.'+barcode_sequence_name,
            'implementation': 'standard',
            'prefix': prefix,
            'padding': 13,
            'number_increment': 1,
            'number_next': 1,
            
        })
        return self.env['ir.sequence'].next_by_code('barcodesequence.'+barcode_sequence_name)
    
           