
from odoo.exceptions import UserError
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class EDITag(models.Model):
    _name = 'edi.tag'
    _description = 'Wrapper class for a field and the corresponding XML tag'

    is_static = fields.Boolean(string="Static",
                               help="Check this box if this element's text should be constant across all records and not be read from any field")
    static_content = fields.Char(string="Static Element Content",
                                 help="The text content that you want to appear in this element across all records")

    xml_tag = fields.Char(string="XML Tag",
                          required=True,
                          help="Enter the XML tag that will wrap around this element (e.g. 'product' would export it like '<product></product>' in the XML)")

    model = fields.Integer(string="Model",related="custom_mapping.model.id", store=True) #child elements dont correctly maintain the model or mapping

    field_id = fields.Many2one(comodel_name="ir.model.fields",
                               string="Fields",
                               help="Select which field for this model this tag will apply to (leave empty if this is just a wrapping tag)",
                               domain="[('model_id','=',model)]")


    child_tag_ids = fields.One2many(comodel_name="edi.tag",
                                   string="Child Elements",
                                   inverse_name="parent_tag_id",
                                   help="Add child elements to this tag")

    number_of_children = fields.Integer(string="Number of Children",
                                        compute="_compute_number_of_children")

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

    #If the user checks is_static, make sure we clear the field and field tree
    @api.onchange("is_static")
    def change_static(self):
        if self.is_static:
            self.field_id = False
            self.field_tree = False
        else:
            self.static_content = False

    
    @api.depends("child_tag_ids")
    @api.onchange("child_tag_ids")
    def _compute_number_of_children(self):
        for record in self:
            record.number_of_children = len(record.child_tag_ids)




    @api.onchange("field_tree")
    def get_field_object_from_tree(self):
        # When the user enters a field tree, it attempts to traverse the tree and retrieve the specified ir.models.field object in order to:
        # (1) make sure it exists, and
        # (2) be able to display metadata about the field and behave accordingly (i.e. the ttype)

        if self.field_tree:
            #Children do not directly belong to the mapping, so they don't have a custom_mapping set,
            #But we need to know what mapping we are a descendant of to get the model. So traverse up the parent tree until we know the mapping.
            #(Don't set self.custom_mapping to the parent's custom_mapping because then the child will also become a sibling to the parent.)
            this_element = self
            while not this_element.custom_mapping:
                this_element = this_element.parent_tag_id
            mapping = this_element.custom_mapping

            path = self.field_tree.split("/") # path is now a list of field names in order, ie ['field1','field2']

            #get the first field of the path from the model
            this_field = self.env["ir.model.fields"].search([("model_id.model","=",mapping.model.model),("name","=",path[0])])

            #traversing the field path
            last_model=mapping.model.model #for raising error if the field path is wrong
            path_index=0
            for path_index in range(1,len(path)): # go 1 subfield deeper each iteration
                #print("Current field:",this_field.name)
                #print("Searching model", this_field.relation, "for field", path[path_index])

                last_model = this_field.relation
                this_field = self.env["ir.model.fields"].search([("model_id.model","=",this_field.relation),("name","=",path[path_index])])

                #this_field will be False if no field by this name exists in this model
                if not this_field:
                    break

            if this_field:
                #print("This_field:",this_field.name)
                self.field_id = this_field
            else: #path must not have been valid
                raise UserError("Field traversal failed: Model '" + last_model +
                                "' has no field '" + path[path_index] + "'. Are you sure you entered the right path? :P")



    