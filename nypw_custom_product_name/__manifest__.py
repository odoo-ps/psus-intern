# -*- coding: utf-8 -*-
{
    'name': "NYPW update product name",

    'summary': """
        This module is used to update the product name based on the product category selected and also create a UPC number based on the selected product gender""",

    'description': """
        This module is used to update the product name based on the product category selected
        Ticket No : 2873874
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
