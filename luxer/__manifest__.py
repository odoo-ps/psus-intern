# -*- coding: utf-8 -*-
{
  'name': 'Luxer',
  'summary': '''Luxer copy contact info''',
  'description': '''
    Add the partner's adress to the invoice
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Sales',
  'version': '15.0.0',
  'depends': [
    'sale_subscription',
    'sale'
  ],
  'data': [
    'views/subscription_view_inherit.xml',
    'views/invoice_form_inherit.xml'
  ],
  'license': 'OPL-1'
}
