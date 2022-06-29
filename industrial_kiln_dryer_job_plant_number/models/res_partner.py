# -*- coding: utf-8 -*-

from re import findall
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    plant_code_id = fields.Many2one(comodel_name='plant.code')

    def next_plant_code(self):
        if not self.plant_code_id:
            company_prefix = ''.join(findall("[a-zA-Z]", self.commercial_company_name or self.name)[:3]).upper()
            
            # check if a sequence already exists with the company prefix
            existing_seq = self.env['plant.code'].search([('company_prefix', '=', company_prefix)])
            if existing_seq:
                self.plant_code_id = existing_seq.id

            # otherwise create a new sequence
            else:
                self.plant_code_id = self.env['plant.code'].create({
                    'name': f'Plant Code: {company_prefix}',
                    'company_prefix': company_prefix
                    })

        return self.plant_code_id.next_plant_code()