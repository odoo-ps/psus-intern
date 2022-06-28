# *-* coding: utf-8 *-*
from odoo import models,fields,api


class MRPProduction(models.Model):
    _inherit = "mrp.production"
    lot_number_prefix = fields.Char(string="Lot number prefix", help="Prefix for the lot number")
    code = fields.Char(string='Sequence Code')
    
    def button_mark_done(self):
    
        res = super(MRPProduction, self).button_mark_done()
        
        if not self.lot_number_prefix:
            self.lot_number_prefix = self.env['ir.sequence'].next_by_code(self.product_id.lot_number_prefix)     
            
            if not self.lot_number_prefix:
                self.lot_number_prefix = self.env['ir.sequence'].create({
                    'name': 'Lot Number Prefix',
                    'code': self.product_id.lot_number_prefix,
                    'prefix': self.product_id.lot_number_prefix,
                    'padding': 5,
                    'number_increment': 1,
                    'company_id': self.company_id.id,
                    'implementation': 'standard',
                }).next_by_code(self.product_id.lot_number_prefix)
        return res
    
    