
from odoo import models, fields, api


class MRPProduction(models.Model):
    _inherit='mrp.production'

    lot_number = fields.Char(string="Specific Lot Number")

    def button_mark_done(self):
        res = super(MRPProduction, self).button_mark_done()
        

