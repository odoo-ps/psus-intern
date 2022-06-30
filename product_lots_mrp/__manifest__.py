{
    'name': 'Product Specific Lots',
    'summary': """
            This module adds lot numbers that correlate with the product for record keeping purposes""",
    'description': """
        Lot numbers are assigned with nomenclature based on the product and are serialized based off of that item.
        1) Nomenclature based on products

            1.1) Assigned on product (currently no variants)
            1.2) Apply the correct lot number name at the end of the manufacturing process (same as current lot number process)
        

        2) Odoo keeps track of what lot number per product is next

            2.1) When lot number is assigned it counts up based off of the last number with that item's nomenclature
            2.2) User should be able to add the new lot number with click (same as + icon in the manufacturing process)

        task id: 2874233
    """,
    'author': 'Odoo',
    'website': 'odoo.com',
    'category': 'Training',
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['mrp'],
    'data': [
        'views/product_template_views_inherit.xml',
        'views/mrp_production_views_inherit.xml',
    ],
}
