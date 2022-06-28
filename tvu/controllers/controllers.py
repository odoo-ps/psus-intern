# -*- coding: utf-8 -*-
# from odoo import http


# class Tvu(http.Controller):
#     @http.route('/tvu/tvu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tvu/tvu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tvu.listing', {
#             'root': '/tvu/tvu',
#             'objects': http.request.env['tvu.tvu'].search([]),
#         })

#     @http.route('/tvu/tvu/objects/<model("tvu.tvu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tvu.object', {
#             'object': obj
#         })
