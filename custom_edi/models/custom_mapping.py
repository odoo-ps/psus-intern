from odoo import models, fields, api
import logging
from lxml import etree as ET

_logger = logging.getLogger(__name__)


class CustomMapping(models.Model):
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

    _name = "edi2.custom.mapping"
    _description = "Custom Mapping"

    root_tag = fields.Char(string="Root Tag", required=True, help="The XML tag of the root element")
    record_tag = fields.Char(string="Record Tag", required=True, help="The wrapping XML tag to go around each individual record")

    record_document_mode = fields.Selection(string="Record exporting mode",
                                            selection=[("all_records", "All records go in one big XML document"),
                                                       ("one_record", "Each record gets its own XML document")],
                                            default="all_records",
                                            required=True)

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
        print(m)

        return

    @api.onchange("model")
    def filt(self):
        # If the user changes the model, the tags will clear because any fields selected will no longer be applicable to the selected model
        self.edi_tag = [(5, 0, 0)]


######################### XML exporting

# TODO: Add support for exporting fields that are one2many, wherein we have to iterate over each record belonging to that one2many
#       (refer to the exported 940 documents and jot's 940 document template where he does that)
# X Add option to export each record into their own document instead of putting all records in the same 1 document
# X If a field in a record has a value of "false" when its ttype is not boolean, it means it's not set so do not put the "false" in the xml
# X Format dates when exporting
# X ability to add "static tags" (tags that contain text that are the same for all records and don't depend on any field)

    def export(self):
        # Runs through all fields/tags given in this mapping and exports them into a XML called testfile.xml in the odoo dir
        # (subfields are specified using paths in the "field tree" field)

        root = ET.Element(self.root_tag)

        tech_name = self.model.model
        all_records = self.env[tech_name].search([]) #all records of the model (e.g. all products)

        file_num = 0
        for record in all_records:

            record_element = ET.SubElement(root, self.record_tag)

            print("******************** RECORD *********************")

            for tag in self.edi_tag:

                tag_element = ET.SubElement(record_element, tag.xml_tag)
                
                if tag.is_static:
                    tag_element.text = tag.static_content
                else: #only non-static fields get their set fields evaluated
                    if tag.field_id or tag.field_tree: #this tag contains a field
                        self.add_field(tag_element, tag, record)
                
                if len(tag.child_tag_ids) > 0: #this tag contains children tags that we must process
                    self.add_children_tags(tag_element, tag, record)

                #end `for tag`

            # user wants only one record per document
            if self.record_document_mode=="one_record":
                record_root = ET.Element(self.root_tag)
                record_root.append(record_element)
                with open("myxmls/testfile" + str(file_num) + ".xml", "wb") as file:
                    file.write(ET.tostring(record_root, pretty_print=True))
                    file_num+=1
            
            #end `for record`

        # user wants all records in one document
        if self.record_document_mode=="all_records":
            with open("myxmls/testfile.xml","wb") as file: #ends up in the base odoo directory
                file.write(ET.tostring(root, pretty_print=True))

        return
    

    def add_field(self, root, tag, record):
        # Fetches the field data specified by the `tag` for `record` and adds it to `root`
        #
        # root - root ET element object to add field to
        # tag - EDI tag object whose selected field we're getting
        # record - current record whose data we're exporting (this method is meant to be called from the main loop as it only processes 1 record)


        if tag.field_tree: #if a field tree is set

            path = tag.field_tree.split("/") # path is now a list of field names in order, ie ['field1','field2']
            name_path = tag.field_tree #for printing

            this_field = self.env["ir.model.fields"].search([("model_id.model","=",self.model.model),("name","=",path[0])])
            this_value = record[path[0]]

            for path_index in range(1,len(path)): # go 1 subfield deeper each iteration
                this_value = this_value[path[path_index]]
                this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.model),("name","=",path[path_index])])

            #at end of loop we should be at the final field of the path.
            #this_value holds the actual data of the final field (ie the string, or the int, or whatever it is; shouldn't be relational)
            #this_field holds the field object of the final field (ir.model.fields instance)

        elif tag.field_id: #there is no tree but there is a field
            this_field = tag.field_id #the actual 'field' obj of the tag model set by the user (only gets used if there is no tree, so this should be non relational)
            this_value = record[this_field.name]
            name_path = this_field.name
                
        print("~~~~~ Field: " + name_path + " ~~~~~")
        print("Value: " + str(this_value))
        print("Tag: " + str(tag.xml_tag))

        print("Ttype:", this_field.ttype)
        print("Py type:", type(this_value))

        #date formatting to YYYY-MM-DD
        if this_value and (this_field.ttype=="date" or this_field.ttype=="datetime"): #field has a value, and is a date type
            this_value = this_value.strftime('%Y-%m-%d')

        #if this field is set to "False" but it's NOT supposed to be a Boolean field, it's probably just not set, so don't export it
        if not (this_value==False and this_field.ttype!="boolean"):
            root.text = str(this_value)

        return

    def add_children_tags(self, root, parent_tag, record):
        # Recursively adds the children tags of `parent_tag` to the document, inside element `root`
        #
        # root - ET Element object; the XML element that we want to add the children to
        # parent_tag - EDI tag object whose children we want to add to the XML
        # record - current record whose data we're exporting (this is meant to be called from the main loop as it only processes 1 record)

        for child_tag_id in parent_tag.child_tag_ids:
            new_child_tag = ET.SubElement(root, child_tag_id.xml_tag)

            if child_tag_id.field_id or child_tag_id.field_tree: #if this child has a field OR a field tree set
                self.add_field(new_child_tag, child_tag_id, record)

            if len(child_tag_id.child_tag_ids) > 0: #if this child tag has children of its own, add all those children, and their children, and their children etc etc
                self.add_children_tags(new_child_tag, child_tag_id, record)
        return
