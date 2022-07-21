
from odoo.exceptions import UserError
from odoo import models, fields, api

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


    #child elements dont maintain model or mapping, only top level elements (direct children of the root) do
    model = fields.Integer(string="Model",related="custom_mapping.model.id", store=True)
    custom_mapping = fields.Many2one(comodel_name='edi2.custom.mapping', readonly=True)

    field_id = fields.Many2one(comodel_name="ir.model.fields",
                               string="Field",
                               help="Select which field for this model this tag will apply to (leave empty if this is just a wrapping tag)",
                               domain="[('model','=',model_name)]")

    child_tag_ids = fields.One2many(comodel_name="edi.tag",
                                   string="Child Elements",
                                   inverse_name="parent_tag_id",
                                   help="Add child elements to this tag")

    number_of_children = fields.Integer(string="Number of Children",
                                        compute="_compute_number_of_children")

    parent_tag_id = fields.Many2one(comodel_name="edi.tag",
                                    string="Parent Element",
                                    help="The element that this element is a child of")

    ### for edi_tags that have a x2many field as their field_id
    x2many_record_tag = fields.Char(string="X2many Record Tag",
                                  help="XML tag to wrap around each individual X2many record")
    x2many_subtag_ids = fields.One2many(comodel_name="edi.tag",
                                       string="X2many Subtags To Export",
                                       help="Specify what fields to export for every record in the X2many",
                                       inverse_name="x2many_field_parent_id")
    x2many_field_parent_id = fields.Many2one(comodel_name="edi.tag")
    ############
    
    relation = fields.Char(string="Related Model", related="field_id.relation")

    ttype = fields.Selection(string="Type", related="field_id.ttype", store=True)

    field_description = fields.Char(string="Description", related="field_id.field_description")


    #-------------------------------------------------------------

    model_name = fields.Char(string="Model", related="custom_mapping.model.model", store=True, readonly=True)
    field_path = fields.Char(string="Field Path", readonly=True,
                       help="""String that represents the path to the subfield from the base model using periods as 
                               separators. Example: If the base model is mail.channel and the subfield is Color Index 
                               on res.groups, field_path = 'group_ids.color'"""
                       )
    parent_model = fields.Char(string="Parent Model", related="field_id.model", readonly=True,
                               help="""String that represents the Parent Model of the field (and not the Base Model) 
                                       of the mapping. Example: If the base model is mail.channel and the subfield is 
                                       Color Index on res.groups, parent_model = 'res.groups'"""
                               )

    # If the user checks is_static, make sure we clear the field and field tree
    @api.onchange("is_static")
    def change_static(self):
        if self.is_static:
            self.field_id = False
            self.field_path = False
        else:
            self.static_content = False

    
    @api.depends("child_tag_ids")
    @api.onchange("child_tag_ids")
    def _compute_number_of_children(self):
        for record in self:
            record.number_of_children = len(record.child_tag_ids)

    # TODO: Might be obselete now that we automatically fetch the field_path using the context. Can be kept to allow both
    #       functionalities??
    @api.onchange("field_path")
    def get_field_object_from_tree(self):
        # When the user enters a field tree, it attempts to traverse the tree and retrieve the specified ir.models.field object in order to:
        # (1) make sure it exists, and
        # (2) be able to display metadata about the field and behave accordingly (i.e. the ttype)
        # If it finds it, it sets it as self.field_id for quick reference (BUT the tree is still needed for the correct path TO the field!)
        #
        # This whole method probably won't be needed once we can get the subfield-selection working.

        if self.field_path:

            ############### Get the mapping that this edi tag belongs to so we can access its model
            # Children do not directly belong to the mapping, so they don't have a custom_mapping set,
            # But we need to know what mapping we are a descendant of in order to get the model.
            # So traverse up the parent tree until we get to a root tag that has it.
            #
            # (Don't set self.custom_mapping to the parent's custom_mapping because then the child will also become a sibling to the parent.
            this_element=self
            while not this_element.custom_mapping:
                if this_element.parent_tag_id:
                    parent=this_element.parent_tag_id
                else: # this_element.x2many_field_parent_id:
                    parent=this_element.x2many_field_parent_id
                if not parent:
                    print("********************************* error")
                    #should not get here because if something doesnt have a custom_mapping, then it has to be a child of SOMETHING
                this_element=parent
            mapping=this_element.custom_mapping


            path = self.field_path.split("/") # path is now a list of field names in order, ie ['field1','field2']

            print(self.parent_tag_id.ttype)
            print("XML tag:",self.xml_tag)
            print("Parent:",self.parent_tag_id)
            print("X2M parent:", self.x2many_field_parent_id)


            ################### get full path for x2m subfields
            # X2Many subfields have a truncated field_path path where whatever's in the path field applies to the parent X2Many's path
            # i.e. a path of "created_date" that is in a subfield of a X2Many with a path of "activity_ids" is really a full path of "activity_ids/created_date"
            if self.x2many_field_parent_id:
                if self.x2many_field_parent_id.field_path:
                    parent_path = self.x2many_field_parent_id.field_path.split("/")
                else:
                    parent_path = [self.x2many_field_parent_id.field_id.name]
                path = parent_path + path
                print(path)
                #self.field_path = path
            

            ################### now traverse the full path and find the field object.

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
                self.ttype = this_field.ttype
            else: #path must not have been valid
                raise UserError("Field traversal failed: model '" + last_model +
                                "' has no field '" + path[path_index] + "'. Are you sure you entered the right path? :P")

    # ADD Children EDI Tags
    def add_children(self):
        ctx = self.env.context.copy()
        # If the current tag is not a child of another, assign it as the parent
        if self.custom_mapping:
            ctx['parent_mapping'] = self.custom_mapping.id
        ctx['parent_edi_tag'] = self.id
        # Parse all the way up from a child to get the base model name, using the parent tags to traverse
        model = self.model_name
        parent = self.parent_tag_id
        while parent:
            model = parent.custom_mapping.model.model
            parent = parent.parent_tag_id

        return {
            'name': model,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'ir.model.fields',
            'domain': [('model', '=', model)],
            'view_mode': 'tree',
            'target': 'new',
            'context': ctx,
        }