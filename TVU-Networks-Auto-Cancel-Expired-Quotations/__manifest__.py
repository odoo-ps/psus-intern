# -*- Coding: utf-8 -*-
{
  'name': 'Auto-remove quotations',
  'summary': '''Administrative app to auto cancel expired quotations''',
  'description': '''
    Every night at midnight, cancel all quotations where the expiration date is before the current day.
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Administrative',
  'version': '15.0.1.0.0',
  'depends': ['sale'],
  'license': 'OPL-1'
}
