# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

# Create a Scheduled Action that will confirm all RFQs into PO given partner_id = Mindesa SAPI de CV (id = 1 in res.partner) and user_id = OdooBot (id = 1 in res.users).

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # _name = 'transfer.rfqs.to.po'

    def _transfer_rfqs_to_po(self):
        rfq_ids = self.env['purchase.order'].search([('partner_id', '=', 1), ('state', '!=', 'draft'), ('user_id', '=', 1)])
        for rfq in rfq_ids:
            rfq.button_confirm()