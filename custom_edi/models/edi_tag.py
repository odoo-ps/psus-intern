
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class EDITag(models.Model):
    _name = 'edi.tag'
    _description = 'Wrapper class for a field and the corresponding XML tag'

    xml_tag = fields.Char(string="XML Tag", required=True)

    model = fields.Integer(string="Model", related="custom_mapping.model.id", store=True)

    field_id = fields.Many2one(comodel_name="ir.model.fields",
                               string="Fields",
                               help="Select which fields for this model you want to put in your document :)",
                               domain="[('model_id','=',model)]")
    
    #field_id2 = fields.Many2one(comodel_name="ir.model.fields",
    #                            string="Fields2")
    #                            #domain="[('model_id','=',field_id.related)]")

    child_tag_ids = fields.One2many(comodel_name="edi.tag",
                                   string="Child Tags",
                                   inverse_name="parent_tag_id")

    parent_tag_id = fields.Many2one(comodel_name="edi.tag",
                                    string="Parent Tag")
                                    


    custom_mapping = fields.Many2one(comodel_name='edi2.custom.mapping')
    ttype = fields.Selection(string="ttype", related="field_id.ttype")
    relation = fields.Char(string="Related Model", related="field_id.relation")
    field_description = fields.Char(string="Description", related="field_id.field_description")

    field_tree = fields.Char(string="Field tree")

    """deprecated & doesnt work
    @api.onchange("field_id")
    def _onchange_field_id(self):
        _logger.error("onchange")
        _logger.error(self.field_id.name)
        _logger.error(self.field_id.related)
        if self.field_id.related:
            return {'domain' : {'field_id2' : [('model_id', '=', self.field_id.related)]}}"""
