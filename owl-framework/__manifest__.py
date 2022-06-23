# -*- coding utf-8 -*-
{
  'name': 'OWL Framework',
  'summary': '''App to do POS Changes''',
  'description': '''
    Customer wants to add selection of a customer type on the client screen on osoo pos.
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Training',
  'version': '15.0.1.0.0',
  'depends':['sale'],
  "data": [
    'views/res_partner_inherit.xml'
  ],
  "assets": {
    'point_of_sale.assets': [
      '/owl-framework/static/src/js/costumer_type.js',
    ],
    "web.assets_qweb":[
      "/owl-framework/static/src/xml/ClientListScreen.xml"
    ],
  },
  'license': 'OPL-1'
}
