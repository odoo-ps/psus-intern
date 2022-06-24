# -*- coding: utf-8 -*-
{
    'name': "Update Product Prices",

    'summary': """
        This module creates two new custom fields for the product template and computes sales based on the newly created fields""",

    'description': """
        This module creates two new custom fields for the product template and computes sales based on the newly created fields
        Ticket No : 2873891
    """,

    'author': "Odoo Inc",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    
    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
       'views/product_template_form_view_inherit.xml'
    ],

    'license': 'OEEL-1'
}
