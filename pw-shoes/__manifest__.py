# -*- Encoding: utf-8 -*-
{
  'name': 'P&W Shoes',
  'summary': '''Autocalculate the price''',
  'description': '''
    NY P&W Shoes is a shoe distributor in New York. They buy shoes in large quantities from China and redistribute them here in the US. They negotiate prices per pair but they sell by case and buy by the case. 
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Administrative',
  'version': '0.1',
  'depends': ['sale'],
  'data': [
    'views/product_form_view_inherit.xml'
  ],
  'license': 'OPL-3'
}
