{
  'name': 'Bottling Experts',
  'summary': '''App to generate custom invoice and quotation report''',
  'description': '''
    Client uses specialized quotation and invoice templates that they are unable to replicated to their requirements in the Studio report editor. This is essential to their    operations in managing complex B2B service requests
  ''',
  'author': 'Odoo',
  'website': 'https://www.odoo.com',
  'category': 'Sales',
  'version': '15.0.1.0.0',
  'depends': ['sale'],
  'data': [
    'views/sale_order_form.xml',
    'report/report_bottling.xml'
  ],
  'license': 'OPL-1'
}
