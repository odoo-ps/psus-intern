# -*- coding: utf-8 -*-
# from odoo import http


# class Order-less-than-demand(http.Controller):
#     @http.route('/order-less-than-demand/order-less-than-demand', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order-less-than-demand/order-less-than-demand/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('order-less-than-demand.listing', {
#             'root': '/order-less-than-demand/order-less-than-demand',
#             'objects': http.request.env['order-less-than-demand.order-less-than-demand'].search([]),
#         })

#     @http.route('/order-less-than-demand/order-less-than-demand/objects/<model("order-less-than-demand.order-less-than-demand"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order-less-than-demand.object', {
#             'object': obj
#         })
