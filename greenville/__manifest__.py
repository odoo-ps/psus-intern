# -*- coding: utf-8 -*-

{

    "name" : "Greenville Produce - Product Lists",

    "summary" : "Adds Product List functionality",

    "description" : """Adds Product Lists:
    -Lists that can be populated with chosen products
    -Users can be delegated to a list
    -Only the products in their list will appear on the shop page for the user
    -If no list is chosen then all products will appear
    """,

    "author" : "Sam Struble",

    "category" : "Training",

    "version" : "0.1",

    "license":"LGPL-3",

    "depends" : ["sale","contacts","website","website_sale"],

    "auto-install":False,

    "installable":True,

    "application":False,

    "data" : [
        "security/ir.model.access.csv",

        "views/sale_menuitems_inherit.xml",
        "views/product_list_view.xml",
        "views/base_view_partner_form_inherit.xml",

    ],

    "demo" : []

}
