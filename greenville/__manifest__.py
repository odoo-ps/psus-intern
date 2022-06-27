# -*- coding: utf-8 -*-
{
  'name': 'Greenville Producer',
  'summary': '''Unique product lists per customer on website''',
  'description': '''
    Module to only show them products that they would buy and nothing unrelated. 
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Sales',
  'version': '14.0.1.0.0',
  'depends': [
    'sale',
  ],
  'data': [
    'security/productlist_security.xml',
    'security/ir.model.access.csv',
    'views/product_list_menuitem.xml',
    'views/product_list_view.xml',
    'views/res_partner_form_view_inherit.xml'
  ],
  'license': 'OPL-1'
}

