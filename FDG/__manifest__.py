# -*- coding: utf-8 -*-
{
  'name': 'FGD Glass Solutions  ',
  'summary': '''Access rights changes''',
  'description': '''
    Access rights module to manage the access rights of the users:
    Sales/all group after creating a new user they cannot will be able to change the sales person o pricelist of them
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Training',
  'version': '0.1',
  'depends': ['sale'],
  'data': [
    'views/res_partner_inherit.xml',
    'security/ir.model.access.csv'
  ],
  'license': 'OPL-1'
}
