# -*- coding: utf-8 -*-
{
    'name': "NY P&W Shoes - Case Structure",

    'summary': """
        Module allowing buying and selling of shoes in the form of a case (collection of shoe pairs)
        """,

    'description': """
        Implemented the task with taskid 2873961.
        Created additional fields to store the number of shoes present in a case and then the price for each pair
        and then computed the total price based on this case. The total price field is only editable when the
        price for the case is 0.
    """,

    'author': "Odoo Inc.",
    'website': "http://www.odoo.com",
    
    'category': 'Product',
    'version': '1.0',

    'depends': ['sale'],

    'data': [
        'views/product_template_form.xml',
    ],

    'license': 'OPL-1'
}
