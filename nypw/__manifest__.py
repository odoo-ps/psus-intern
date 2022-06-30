# -*- coding: utf-8 -*-
{
    'name': "New York P&W: Automated Product Name & UPC",

    'summary': """
        Module to generate product names automatically based on product category based sequences""",

    'description': """
        Taskid: 2873944
        Created a Many2one field from product category mapping to the sequence and generating a
        sequence whenever a product is created under a product category. Then we autoassign the
        product name based on the sequence generated using the product category. This name is
        unique and follows the exact same rules of Odoo nomenclature.
    """,

    'author': "Odoo Inc.",
    'website': "http://www.odoo.com",

    'category': 'Products',
    'version': '1.0',

    'depends': ['sale'],

    'license': 'OEEL-1'
}
