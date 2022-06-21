# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inventory_receipts_validation(models.Model):
#     _name = 'inventory_receipts_validation.inventory_receipts_validation'
#     _description = 'inventory_receipts_validation.inventory_receipts_validation'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
