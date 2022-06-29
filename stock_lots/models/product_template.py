import re
from odoo import models, fields, api, _

# X is the wildcard character, but otherwise anything can go before and after a string of X's.
LOT_TEMPLATE_PATTERN = re.compile('^([^X]*)(X+)([^X]*)$')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lot_no_template = fields.Char('Lot Number Template')
    lot_no_prefix = fields.Char(
        'Lot Number Prefix', compute='_compute_lot_no', store=True)
    lot_no_suffix = fields.Char(
        'Lot Number Suffix', compute='_compute_lot_no', store=True)
    lot_no_padding = fields.Integer(
        'Lot Number Padding', compute='_compute_lot_no', store=True)

    @api.constrains('lot_no_template')
    def _check_lot_no_template(self):
        for product in self:
            if product.lot_no_template and LOT_TEMPLATE_PATTERN.match(product.lot_no_template) is None:
                raise models.ValidationError(
                    _('Lot Number Template must contain exactly one uninterrupted string of X characters.'))

    @api.depends('lot_no_template')
    def _compute_lot_no(self):
        for product in self:
            if product.lot_no_template:
                match = LOT_TEMPLATE_PATTERN.match(product.lot_no_template)
                product.lot_no_prefix = match.group(1)
                product.lot_no_suffix = match.group(3)
                product.lot_no_padding = len(match.group(2))
            else:
                product.lot_no_prefix = ''
                product.lot_no_suffix = ''
                product.lot_no_padding = 0
