# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Automated Product Name & UPC",
    'summary': """Generates unique product names and UPCs.""",
    'description': """
        A customer generates product names when ordering new products
        from the suppliers. The unique product name is a code linked
        to a product category. A UPC is also generated automatically.
        The customer can then send the UPC to the manufacturer and
        print it on the labels.

        Task ID: 2873664
        """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Sales',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['product'],
    # always loaded
    'data': ['views/product_template_views.xml'],
    'application': False
}
