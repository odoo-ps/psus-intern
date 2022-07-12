
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ModelField(models.Model):
    _inherit = "ir.model.fields"

    xml_tag = fields.Char(name="XML Tag", description="XML Tag to use in EDI", stored=True)

    #button to print subfields of this field (only on o2m, m2m, m2o)
    def get_subfields(self):
        submodel = self.relation #get the related model (STRING of the technical model name)

        subfields = self.env["ir.model.fields"].search([("model_id.model","=",submodel)]) #get all fields where the field belongs to the submodel

        m = "ALL Fields in sub-model " + submodel + ": "
        for field in subfields:
            m = m + field.name + ", "
        
        _logger.error(m)


    # is called to open the "view fields" form on sub-fields
    def open_form(self):
        
        #if "field_tree" in self.env.context:
        #    self.env.context["field_tree"] += "/" + str(self.id)
        #else:
        #    self.env.context["field_tree"] = str(self.id)
        
        #if "field_tree" in self.env.context:
        #    self = self.with_context({"field_tree" : self.env.context["field_tree"]+"/"+str(self.id)})
        #else:
        #    self = self.with_context({"field_tree": str(self.id)})


        #Adds a new variable to the context to keep track of the hierarchy of subfields so we can add it
        # is like this: [ top_model_id, second_model_id, third_model_id, etc ]
        ctx = self.env.context.copy()
        if "field_tree" in ctx:
            ctx["field_tree"].append(self.id)
        else:
            ctx["field_tree"] = [self.id]
            
        return {
            #'name': 'Fields',
            'name': self.field_description,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'ir.model.fields',
            'domain': [('model_id', '=', self.relation)],
            'view_mode': 'tree',
            'target': 'current',
            'res_id' : self.id,
            'context' : ctx
        }
    def add(self):
        _logger.error("Add button pressed on " + self.field_description)
        #_logger.error(self.env.context)
        #_logger.error("Field Tree: " + str(self.env.context["field_tree"]))

        if "field_tree" in self.env.context:
            m="FIELD TREE: "
            for model_id in self.env.context["field_tree"]:
                m = m + self.env["ir.model.fields"].browse(model_id)[0].field_description + "/"
            _logger.error(m)

            #self.field_tree = "/".join(str(self.env.context["field_tree"]))

        #return {'type': 'ir.actions.act_window_close'}
