
from odoo import models, fields, api

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

    model = fields.Many2one(comodel_name="ir.model",string="Models")

