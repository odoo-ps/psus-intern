
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

    #fields = {}

    # IF THE MODEL CHANGES, REFETCH THE MODEL'S FIELDS
    @api.onchange("model")
    def get_fields(self):
        _logger.error("Model name: " + str(self.model.name))
        try:
            _logger.error("Model model: " + str(self.model.model)) #model model is a str describing the technical name of the model!
        except Exception as e:
            _logger.error(":-( Model model threw error " + str(e))

        dic = self.model.fields_get(allfields=[],attributes=["string","help","type"])
        #_logger.debug(str(self.fields))

        fields = "Fields on top model: "
        for key in dic:
            fields = fields + str(key) +", "
        
        _logger.error(fields)


