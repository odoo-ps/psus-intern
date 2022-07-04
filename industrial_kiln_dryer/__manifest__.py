{
  'name': 'Industrial Kil & Dryer Group',
  'summary': '''Automatically assign job number and plant code''',
  'description': '''
    Automatically assign job number and plant code. On Sale Order (SO), assign job number based on a chosen prefix.
    On Customers, when their first SO is confirmed they will be assigned a plant code based on their company's name.
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': '',
  'version': '14.0.1.0.0',
  'depends': ['sale'],
  'data': [
    'views/res_partner_form.xml',
    'views/sale_order_form.xml'
  ],
  'license': 'OPL-1'
}
