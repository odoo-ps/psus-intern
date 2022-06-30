{
  'name':'Bottling Experts',

  'summary':'''An specialized quotation and invoice template''',

  'description':'''
     Client uses specialized quotation and invoice templates that they are unable 
     to replicated to their requirements in the Studio report editor.
     This is essential to their operations in managing complex B2B service requests.
  ''',

  'author':'Odoo PS',
  
  'category':'Sales',

  'website':'https://www.odoo.com',
  
  'version':'15.0.1.0.0',

  'depends':[
  	'sale',
  ],

  "data":[
    'views/sale_order_views.xml',
    'report/sale_order_report_templates.xml',
  ],
  
   'license':'OPL-1',
}
