from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    plant_code = fields.Char(string='Plant Code', readonly=True)

    def _get_plant_code(self):
        for partner in self:
            if partner.plant_code:
                pass
            elif(partner.commercial_company_name):
                prefix = ''.join(
                    filter(str.isalnum, partner.commercial_company_name)).upper()[:3]
                sequence = self.env['ir.sequence'].next_by_code(prefix)
                if not (sequence):
                    sequence = self.env['ir.sequence'].create({
                        'name': 'Secuence for Plant Code',
                        'code': prefix,
                        'prefix': prefix,
                        'suffix': '',
                        'padding': 5,
                        'implementation': 'standard',
                        'number_next': 1,
                        "number_increment": 1,
                        "active": True,
                    }).next_by_code(prefix)
                sequence = str(sequence[:6]) + '-' + str(sequence[6:])
                partner.plant_code = sequence
            else:
                partner.plant_code = False
