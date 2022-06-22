# -*- coding: utf-8 -*-
# from odoo import http


# class ProductConfigFiberMountain(http.Controller):
#     @http.route('/product_config_fiber_mountain/product_config_fiber_mountain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_config_fiber_mountain/product_config_fiber_mountain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_config_fiber_mountain.listing', {
#             'root': '/product_config_fiber_mountain/product_config_fiber_mountain',
#             'objects': http.request.env['product_config_fiber_mountain.product_config_fiber_mountain'].search([]),
#         })

#     @http.route('/product_config_fiber_mountain/product_config_fiber_mountain/objects/<model("product_config_fiber_mountain.product_config_fiber_mountain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_config_fiber_mountain.object', {
#             'object': obj
#         })
