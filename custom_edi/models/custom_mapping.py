
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class CustomMapping(models.Model):
    _name = "edi2.custom.mapping"
    _description = "Custom Mapping"

    # for exporting odoo records to xml documents
    #
    # user should be able to pick the record type, then there is a one2many field allowing them to add fields they want in the xml.
    # then for each field can type in the XML tag they want associated with that field.
    # I think we should also have presets of a couple document types like the one jot has programmed,
    # where you can pick a preset from a dropdown and it populates each field with how that specific document is exported,
    # and users can edit them and save them as new custom document types
    #
    # maybe they can even rearrange the order of how each field goes into the xml document with drag n drop (or just giving
    # the order with a number) ???


    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

    #one mapping can only use one model, but one model may be in many mappings :)
    model = fields.Many2one(comodel_name="ir.model",string="Model",help="Select the model whose records you wish to export to the xml document.")

    #fields = fields.Many2one(comodel_name="ir.model.fields",string="Fields",help="Select which fields for this model you want to put in your document.")
    # ^^ gets ALL fields of ALL models (over 7000 fields)

    fields = fields.Many2one(comodel_name="ir.model.fields",
                             string="Fields",
                             help="Select which fields for this model you want to put in your document :)",
                             domain="[('model_id','=',model)]")
    # ^^ only shows fields of the model that is currently selected :)



    # IF THE MODEL CHANGES, REFETCH THE MODEL'S FIELDS
    @api.onchange("model")
    def get_fields(self):
        _logger.error("Model name: " + str(self.model.name))
        _logger.error("Model model: " + str(self.model.model)) #model model is a str describing the technical name of the model!

        #dic = self.model.fields_get(allfields=[],attributes=["string","help","type"]) #Gets fields for the BASE model (not very useful :P )

        field_ids = self.model.field_id #gets fields for the model we actually want, as a set of ir.model.fields objects
        #_logger.error(str(field_ids))

        m = "Fields for " + str(self.model.model) + ": "
        for id in field_ids:
            m = m + str(id.name) + ", "

        _logger.error(m)