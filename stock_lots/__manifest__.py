{
    'name': 'Product Specific Lots',
    'version': '1.0',
    'description': 'Product Specific Lots',
    'summary': 'Product Specific Lots',
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': [
        'stock', 'mrp'
    ],
    'data': [
        'views/product.xml',
        'views/mrp.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
