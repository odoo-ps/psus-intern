{
    'name': 'New York P&W : Automated product name & UPC',
    'summary': """Module to create unique product names and barcodes based on sequences..""",
    'description': """
        The product name needs to be unique and tied to it's category, for each category there has to be a sequence.
        The UPC is tied to the category and gender of the product, it also needs to be unique.
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '14.0.1.0.0',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_template_views_inherit.xml'
    ],
    'license': 'OPL-1',
}
