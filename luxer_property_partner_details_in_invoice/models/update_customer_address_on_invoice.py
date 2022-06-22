# -*- coding: utf-8 -*-
from odoo import models,fields,api

import logging
logger =logging.getLogger(__name__)
class UpdateCustomerAddressOnInvoice(models.Model):
    _inherit='account.move'
    partner_res=fields.Many2one('res.partner',compute='_get_property_partner_id',string='Property Partner',store=True)

    @api.depends('partner_id')
    def _get_property_partner_id(self):
        logger.info("Kusal reached here and the partner id is ")
        
        for rec in self:
        
            res = self.env['sale.subscription'].search([('code','=',rec.invoice_origin)])
            rec.partner_res=res.property_partner
            logger.info("Kusal reached here and the partner id is ")
        logger.info(self.partner_res)