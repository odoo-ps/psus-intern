
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class EDITag(models.Model):
    _name = 'edi.tag'
    _description = 'Wrapper class for a field and the corresponding XML tag'

    xml_tag = fields.Char(string="XML Tag")
    field_id = fields.Many2one(comodel_name="ir.model.fields",
                               string="Fields",
                               help="Select which fields for this model you want to put in your document :)")
    sub = fields.Many2one(comodel_name="ir.model.fields",
                               string="Subfields",
                               help="Select which fields for this model you want to put in your document :)")
    custom_mapping = fields.Many2one(comodel_name='edi2.custom.mapping')
    model = fields.Integer(string="Model", related="custom_mapping.model.id", store=True)
    ttype = fields.Selection(string="ttype", related="field_id.ttype")
    relation = fields.Char(string="Related Model", related="field_id.relation")
    field_description = fields.Char(string="Description", related="field_id.field_description")

    def get_subfields(self):
        submodel = self.relation  # get the related model (STRING of the technical model name)

        subfields = self.env["ir.model.fields"].search(
            [("model_id.model", "=", submodel)])  # get all fields where the field belongs to the submodel

        m = "ALL Fields in sub-model " + submodel + ": "
        for field in subfields:
            m = m + field.name + ", "

        _logger.error(m)

    # def open_form(self):
    #
    #     # if "field_tree" in self.env.context:
    #     #    self.env.context["field_tree"] += "/" + str(self.id)
    #     # else:
    #     #    self.env.context["field_tree"] = str(self.id)
    #
    #     # if "field_tree" in self.env.context:
    #     #    self = self.with_context({"field_tree" : self.env.context["field_tree"]+"/"+str(self.id)})
    #     # else:
    #     #    self = self.with_context({"field_tree": str(self.id)})
    #
    #     # Adds a new variable to the context to keep track of the hierarchy of subfields so we can add it
    #     # is like this: [ top_model_id, second_model_id, third_model_id, etc ]
    #     ctx = self.env.context.copy()
    #     if "field_tree" in ctx:
    #         ctx["field_tree"].append(self.id)
    #     else:
    #         ctx["field_tree"] = [self.id]
    #
    #     return {
    #         # 'name': 'Fields',
    #         'name': self.field_description,
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'res_model': 'ir.model.fields',
    #         'domain': [('model_id', '=', self.relation)],
    #         'view_mode': 'tree',
    #         'target': 'current',
    #         'res_id': self.id,
    #         'context': ctx
    #     }