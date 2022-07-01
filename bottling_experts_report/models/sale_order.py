# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# references:
# https://www.odoo.com/forum/help-1/how-to-create-a-customized-invoice-report-odoo-14-184296
# https://www.youtube.com/watch?v=Szj3vs6V6iQ
# psus-custom: sanmex, softiron, ibalma, eurocustom, crowdestate

# company.py : invoice_terms_html
# terms-template.xml <- terms and conditions
# <div class="oe_structure" id="oe_structure_terms_conditions"/>
# <div class="container oe_website_terms_conditions">
#     <div id="o_terms_conditions">
#         <div t-field="company.invoice_terms_html"/>
#     </div>
# </div>
# report-invoice.xml <- actual invoice document
# report-journal.xml <- journal document (worth looking)
# report-payment-receipt-templates.xml <- payment document (worth looking)
# (under web) webclient-templates.xml <- most basic frontend layouts
# account-invoice-send-views.xml -> .py
# -> account-move.py -> account-report.xml

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_studio_final_client = fields.Many2one(related="partner_id")
    x_studio_opportunity = fields.Char()  # service as a product
    x_studio_opportunity_desc = fields.Char()  # service as a product
    x_studio_travel_in = fields.Date()
    x_studio_travel_out = fields.Date()
