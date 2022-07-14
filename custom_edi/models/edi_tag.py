
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class EDITag(models.Model):
    _name = 'edi.tag'
    _description = 'Wrapper class for a field and the corresponding XML tag'

    xml_tag = fields.Char(string="XML Tag",
                          required=True,
                          help="Enter the XML tag that will wrap around this element (e.g. 'product' would export like '<product></product>' in the XML)")

    model = fields.Integer(string="Model",related="custom_mapping.model.id", store=True)

    field_id = fields.Many2one(comodel_name="ir.model.fields",
                               string="Fields",
                               help="Select which field for this model this tag will apply to (leave empty if this is a wrapping tag)",
                               domain="[('model_id','=',model)]")


    child_tag_ids = fields.One2many(comodel_name="edi.tag",
                                   string="Child Elements",
                                   inverse_name="parent_tag_id",
                                   help="Add child elements to this tag")

    parent_tag_id = fields.Many2one(comodel_name="edi.tag",
                                    string="Parent Element",
                                    help="The element that this element is a child of")
                                    

    custom_mapping = fields.Many2one(comodel_name='edi2.custom.mapping')
    ttype = fields.Selection(string="ttype", related="field_id.ttype")
    relation = fields.Char(string="Related Model", related="field_id.relation")
    field_description = fields.Char(string="Description", related="field_id.field_description")

    field_tree = fields.Char(string="Field tree",
                             help="""String to represent the field chain as a path through relation fields ending with the target field
                             Format: related_1/related_2/target_field (using fields' technical names like "categ_id")
                             Do not include the base model in the path
                             If this field has content, then this path will be used and any contents of field_id will be ignored
                             """)

