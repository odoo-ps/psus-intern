{
    "name" : "Custom EDI",

    "summary" : "Customizable EDI documents",

    "description" : "Adds user customizable EDI document XML mappings to EDI module",

    "author" : "Odoo",
    
    "category" : "Tools",

    "version" : "1.0",

    "license" : "LGPL-3",

    "depends" : ["base_edi","edi_3pl_central"],

    "auto-install" : False,

    "installable" : True,

    #"application" : False,

    "data" : [
            "views/custom_mapping_menuitems.xml",
            "views/custom_mapping.xml",
            # "views/fields_inherit.xml",
            "security/ir.model.access.csv",
            ],

    "demo" : []


}
