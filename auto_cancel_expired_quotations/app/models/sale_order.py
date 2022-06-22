from odoo import models
import logging

logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _cancel_expired_quotations(self):
        self.search([('is_expired', '=', True), ('state', '=', 'draft')]).unlink()
        logger.info("Search Executed")
        logger.info(self)