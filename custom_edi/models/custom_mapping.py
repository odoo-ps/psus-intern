from odoo import models, fields, api
import logging
from lxml import etree as ET

_logger = logging.getLogger(__name__)


class CustomMapping(models.Model):
    _name = "edi2.custom.mapping"
    _description = "Custom Mapping"

    root_tag = fields.Char(string="Root Tag", required=True, help="The XML tag of the root element")
    record_tag = fields.Char(string="Record Tag", required=True, help="The wrapping XML tag to go around each individual record")

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


    def add_field(self, root, tag, record):
        # Fetches the field data specified by the tag for record and adds it to root
        #
        # root - root ET tag object to add field to
        # tag - EDI tag object whose selected field we're getting
        # record = current record whose data we're exporting (this is meant to be called from the main loop as it only processes 1 record)


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

        elif tag.field_id: #there is no tree but there is a field
            this_field = tag.field_id #the actual 'field' obj of the tag model set by the user (only gets used if there is no tree, so this should be non relational)
            this_value = record[this_field.name]
            name_path = this_field.name
                
        _logger.error("~~~~~ Field: " + name_path + " ~~~~~")
        _logger.error("Value: " + str(this_value))
        _logger.error("Tag: " + str(tag.xml_tag))


        root.text = str(this_value)
        return

    def add_children_tags(self, root, parent_tag, record):
        # Recursively adds the children tags of parent_tag to the document, inside element root
        #
        # root = ET Element object; the element that we want to add the children to
        # parent_tag = EDI tag object whose children we want to add
        # record = current record whose data we're exporting (this is meant to be called from the main loop as it only processes 1 record)

        for child_tag_id in parent_tag.child_tag_ids:
            new_child_tag = ET.SubElement(root, child_tag_id.xml_tag)

            if child_tag_id.field_id: #if this child has a field set
                self.add_field(new_child_tag, child_tag_id, record)

            if len(child_tag_id.child_tag_ids) > 0: #if this child tag has children of its own, add all those children recursively :)
                self.add_children_tags(new_child_tag, child_tag_id, record)
        return


    def export(self):
        #runs through all fields/tags given in this mapping, prints them to the log, and exports them into a test XML called testfile.xml in the odoo dir
        #(subfields are specified using paths in the "field tree" field)

        root = ET.Element(self.root_tag)

        tech_name = self.model.model
        all_records = self.env[tech_name].search([]) #all records of the model (i.e. all products)
        for record in all_records:

            record_element = ET.SubElement(root, self.record_tag)

            _logger.error("******************** RECORD *********************")

            for tag in self.edi_tag:

                # For testing purposes, the field path is a string in the format of "topfield/subfield/subfield"
                # (dont include the name of the model since that is already given in the model field).
                # For example, "categ_id/name" ran with the selected model as "product.product" gets each product's category's name.
                # The last field in the path should be the NON-RELATIONAL field you want to retrieve the actual value of to export.

                # In this version, if there is a tree set then it is used to find the field and the field_id field is ignored completely

                tag_element = ET.SubElement(record_element, tag.xml_tag)
                if tag.field_id or tag.field_tree:

                    self.add_field(tag_element, tag, record)
                
                # if tag.field_tree: #if a field tree is set

                #     path = tag.field_tree.split("/") # path is now a list of field names in order, ie ['field1','field2']
                #     name_path = tag.field_tree

                #     this_field = self.env["ir.model.fields"].search([("model_id.model","=",self.model.model),("name","=",path[0])])
                #     this_value = record[path[0]]

                #     for path_index in range(1,len(path)): # go 1 subfield deeper each iteration
                #         this_value = this_value[path[path_index]]
                #         #this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.model),("name","=",path[path_index])])[0]
                #         this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.model),("name","=",path[path_index])])
                #         #_logger.error("this_field len: " + str(len(this_field)))
                #         #_logger.error("this_field: " + str(this_field))

                #     #at end of loop we should be at the final field of the path.
                #     #this_value holds the actual data of the final field (ie the string, or the int, or whatever it is; shouldn't be relational)
                #     #this_field holds the field object of the final field (ir.model.fields instance)

                # elif tag.field: #there is no tree but there is a field
                #     this_field = tag.field_id #the actual 'field' obj of the tag model set by the user (only gets used if there is no tree, so this should be non relational)
                #     this_value = record[this_field.name]
                #     name_path = this_field.name
                
                # _logger.error("~~~~~ Field: " + name_path + " ~~~~~")
                # _logger.error("Value: " + str(this_value))
                # _logger.error("Tag: " + str(tag.xml_tag))

                if len(tag.child_tag_ids) > 0:
                    self.add_children_tags(tag_element, tag, record)

                
                #logger.error("Type: " + str(this_field.ttype))

        #_logger.error(ET.tostring(root, pretty_print=True))

        with open("testfile.xml","w") as file: #ends up in the base odoo directory
            file.write(ET.tostring(root, pretty_print=True, encoding="unicode"))

        return