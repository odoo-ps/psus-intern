from odoo import models,fields,api


class ProductTemplate(models.Model):

    _inherit='product.template'
    name = fields.Char('Name', index=True,translate=True,store=True ,required = True)
    
    product_gender = fields.Selection(
        string='Product Gender',
        selection=[('Gender1', 'Gender1'), ('Gender2', 'Gender2'),('Gender3','Gender3')],
        default='Gender1'
    )
    upc_sequence_compute = fields.Many2one(
        name='UPC Sequence',
        comodel_name='ir.sequence',
        ondelete='restrict', 
        compute = '_compute_upc_sequence_mapping',
        store= True,readonly=True)
    upc_sequence = fields.Char(name = 'UPC Sequence',
            store= True,
            compute = '_compute_upc_sequence',
            readonly=True)

    
    @api.model
    def create(self, vals):

        category_id = self.env['product.category'].search([('id','=',vals['categ_id'])])
        vals['name'] = self.env['ir.sequence'].next_by_code(category_id.name) 
        res = super(ProductTemplate, self).create(vals)
        return res

    def write(self, vals):

        if "categ_id" in vals:
            category_id = self.env['product.category'].search([('id','=',vals['categ_id'])])
            vals['name'] = self.env['ir.sequence'].next_by_code(category_id.name) 
            print("after",vals)
        else:
            vals['name'] = self.env['ir.sequence'].next_by_code(self.categ_id.name) 
    
        res = super(ProductTemplate, self).write(vals)
        return res

    @api.depends('product_gender')
    def _compute_upc_sequence_mapping(self):

        for record in self:
            seq = self.env['ir.sequence'].search(
                [('code', '=', record.product_gender)])
            if not seq:
                seq = self.env['ir.sequence'].create({
                    'code': record.product_gender,
                    'name': record.product_gender,
                    'prefix': record.product_gender,
                    'padding': 5,
                    "number_increment":1,
                    "number_next":300000,
                })
            record.upc_sequence_compute = seq

    @api.depends('upc_sequence_compute')
    def _compute_upc_sequence(self):

        for record in self:
            if record.upc_sequence_compute:
                record.upc_sequence = record.upc_sequence_compute.next_by_id()