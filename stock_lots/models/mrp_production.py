from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    lot_no = fields.Char('Lot Number', readonly=True)

    def button_mark_done(self):
        res = super().button_mark_done()
        template = self.product_id.lot_no_template
        if res and template:
            seq = self.env['ir.sequence'].next_by_code(template)
            if not seq:
                seq = self.env['ir.sequence'].create({
                    'name': template,
                    'code': template,
                    'prefix': self.product_id.lot_no_prefix,
                    'suffix': self.product_id.lot_no_suffix,
                    'padding': self.product_id.lot_no_padding,
                }).next_by_code(template)
            self.lot_no = '%s%s%s' % (
                self.product_id.lot_no_prefix, seq, self.product_id.lot_no_suffix)
        return res
