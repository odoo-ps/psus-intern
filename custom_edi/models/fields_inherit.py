
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ModelField(models.Model):
    _inherit = "ir.model.fields"

    xml_tag = fields.Char(name="XML Tag", description="XML Tag to use in EDI", stored=True)

    #button to print subfields of this field (only on o2m, m2m, m2o)
    def get_subfields(self):
        submodel = self.relation #get the related model (STRING of the technical model name)

        subfields = self.env["ir.model.fields"].search([("model_id.model","=",submodel)]) #get all fields where the field belongs to the submodel

        m = "ALL Fields in sub-model " + submodel + ": "
        for field in subfields:
            m = m + field.name + ", "
        
        _logger.error(m)


    # is called to open the "view fields" form on sub-fields
    def open_form(self):
        return {
            #'name': 'Fields',
            'name': self.field_description,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'ir.model.fields',
            'domain': [('model_id', '=', self.relation)],
            'view_mode': 'tree',
            'target': 'new',
            'res_id' : self.id
        }