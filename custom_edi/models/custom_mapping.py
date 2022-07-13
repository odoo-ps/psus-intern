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

    # one mapping can only use one model, but one model may be in many mappings :)
    model = fields.Many2one(comodel_name="ir.model", string="Model",
                            help="Select the model whose records you wish to export to the xml document.")

    edi_tag = fields.One2many(comodel_name='edi.tag', inverse_name='custom_mapping')

    # method I wrote to test the ability to access field data of all records of a model
    # (it is output to the log when you press the "Log Data" button at the bottom of the custom mapping form)
    # NOTE - to get the set of ir.model.field objects for a given model we can use: field_ids = self.model.field_id
    def log_field_data(self):
        tech_name = self.model.model  # model model is a str describing the technical name of the model!

        # field_ids = self.model.field_id #gets fields for the model we actually want, as a set of ir.model.fields objects

        all_records = self.env[tech_name].search([])  # all the records of the model the user picked
        m = "ALL Record Names in model " + str(self.model.name) + ": "

        for record in all_records:
            m = m + str(record.name) + "; "
        _logger.error(m)

        _logger.error(self.env.context)
        return

    @api.onchange("model")
    def filt(self):
        self.edi_tag = [(5, 0, 0)]

    
    def export(self): #runs through all fields given and prints them to the log. (subfields are given using paths in the "field tree" field)

        tech_name = self.model.model
        all_records = self.env[tech_name].search([]) #all records of the model (i.e. all products)
        for record in all_records:

            _logger.error("******************** RECORD *********************")

            for tag in self.edi_tag:


                # For testing purposes, the field path is a string in the format of "topfield/subfield/subfield"
                # (dont include the name of the model since that is already given in the model field).
                # For example, "categ_id/name" ran with the selected model as "product.product" gets each product's category's name.
                # The last field in the path should be the NON-RELATIONAL field you want to retrieve the actual value of to export.

                # In this version, if there is a tree set then it is used to find the field and the field_id field is ignored completely

                if tag.field_tree: #if a field tree is set

                    path = tag.field_tree.split("/") # path is now a list of field names in order, ie ['field1','field2']
                    name_path = tag.field_tree

                    this_field = self.env["ir.model.fields"].search([("model_id.model","=",self.model.model),("name","=",path[0])])
                    this_value = record[path[0]]

                    for path_index in range(1,len(path)): # go 1 subfield deeper each iteration
                        this_value = this_value[path[path_index]]
                        #this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.model),("name","=",path[path_index])])[0]
                        this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.model),("name","=",path[path_index])])
                        #_logger.error("this_field len: " + str(len(this_field)))
                        #_logger.error("this_field: " + str(this_field))

                    #at end of loop we should be at the final field of the path.
                    #this_value holds the actual data of the final field (ie the string, or the int, or whatever it is; shouldn't be relational)
                    #this_field holds the field object of the final field (ir.model.fields instance)

                else: #there is no tree
                    this_field = tag.field_id #the actual 'field' obj of the tag model set by the user (only gets used if there is no tree, so this should be non relational)
                    this_value = record[this_field.name]
                    name_path = this_field.name
                
                _logger.error("~~~~~ Field: " + name_path + " ~~~~~")
                _logger.error("Value: " + str(this_value))
                _logger.error("Tag: " + str(tag.xml_tag))
                #logger.error("Type: " + str(this_field.ttype))
        return