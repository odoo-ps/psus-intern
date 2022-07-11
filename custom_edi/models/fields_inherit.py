
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ModelField(models.Model):
    _inherit = "ir.model.fields"

    xml_tag = fields.Char(name="XML Tag", description="XML Tag to use in EDI", stored=True)

    #button to print subfields of this field
    def get_subfields(self):
        submodel = self.relation
        _logger.error(submodel)
        