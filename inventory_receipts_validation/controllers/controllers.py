# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryReceiptsValidation(http.Controller):
#     @http.route('/inventory_receipts_validation/inventory_receipts_validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_receipts_validation/inventory_receipts_validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_receipts_validation.listing', {
#             'root': '/inventory_receipts_validation/inventory_receipts_validation',
#             'objects': http.request.env['inventory_receipts_validation.inventory_receipts_validation'].search([]),
#         })

#     @http.route('/inventory_receipts_validation/inventory_receipts_validation/objects/<model("inventory_receipts_validation.inventory_receipts_validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_receipts_validation.object', {
#             'object': obj
#         })
