# -*- encoding:utf-8 -*-

from odoo import api,models,fields
from odoo.exceptions import AccessError

class modifiedContact(models.Model):
    _inherit = 'res.partner'

    user_id = fields.Many2one(default=lambda self:self.env.user)

    sales_prices = fields.One2many(comodel_name='sale.order',inverse_name='customer_orders')

    #Override the built in write method.
    #Raises error if wrong user group tries to edit salesperson or salesprices field.
    def write(self, vals):
        isAdmin = self.env.user.has_group('fgd_glass.group_fgd_sales_admin')
        if ('user_id' in vals or 'sales_prices' in vals) and not isAdmin:
            raise AccessError('You are attempting to edit a field you do not have access to')
        else:
            res = super(modifiedContact, self).write(vals)
            return res
