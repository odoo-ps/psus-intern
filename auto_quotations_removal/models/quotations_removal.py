from odoo import models

class QuotationsRemoval(models.Model):
    _inherit = 'sale.order'

    def _remove_expired_quotations(self):
        self.search([('is_expired', '=', True),
                    ('state', '=', 'draft')]).unlink()
                    