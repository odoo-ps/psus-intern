
from odoo import models, fields, api

class ModelField(models.Model):
    _inherit = "ir.model.fields"

    xml_tag = fields.Char(name="XML Tag", description="XML Tag to use in EDI", stored=True)
