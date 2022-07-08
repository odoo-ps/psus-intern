
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

    field_ids = fields.Many2many(comodel_name="ir.model.fields",
                             string="Fields",
                             help="Select which fields for this model you want to put in your document :)",
                             domain="[('model_id','=',model)]")
    # ^^ only shows fields of the model that is currently selected :)




    # method I wrote to test the ability to access field data of all records of a model
    # (it is output to the log when you press the "Log Data" button at the bottom of the custom mapping form)
    # NOTE - to get the set of ir.model.field objects for a given model we can use: field_ids = self.model.field_id
    def log_field_data(self):
        tech_name = self.model.model #model model is a str describing the technical name of the model!

        #field_ids = self.model.field_id #gets fields for the model we actually want, as a set of ir.model.fields objects
        
        all_records = self.env[tech_name].search([]) # all the records of the model the user picked
        m = "ALL Record Names in model " + str(self.model.name) + ": "

        for record in all_records:
            m = m + str(record.name) + "; "
        _logger.error(m)
        return


    # If the model is changed while there are fields selected, the field_ids many2many empties since those fields do not belong to the new model.
    @api.onchange("model")
    def clear_fields(self):
        self.field_ids = [(5,0,0)] #Clear command (unlink all records)
        return