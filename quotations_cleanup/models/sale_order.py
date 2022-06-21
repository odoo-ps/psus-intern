from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _unlink_expired_quotations(self):
        self.search([('is_expired', '=', True), ('state', '=', 'draft')]).unlink()