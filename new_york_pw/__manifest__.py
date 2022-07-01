{
  'name': 'New York P&W',
  'summary': '''Automated product name & UPC''',
  'description': '''
    The customer generates product names when he orders new products from the suppliers. The product name is a code and is linked to the product category. Those product names must be unique. The customer also needs to generate UPC automatically. He generates UPC and then sends it back to its manufacturer who will print it on the labels. 
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Training',
  'version': '14.0.1.0.0',
  'depends': ['product'],
  'data': [
    'views/product_category_inherit.xml',
    'views/product_form_inherit.xml'
  ],
  'license': 'OPL-1'
}
