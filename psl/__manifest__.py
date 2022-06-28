# -*- coding: utf-8 -*-
{
  'name':'psl',

  'summary':'''An auto product specific lot setter''',

  'description':'''
    When manufacturing products, the finished goods need to have lot numbers that correlate with the product for record keeping purposes. Additionally due to the volume and daily operations, it needs to be automatically assignable without knowing what the previous lot number for that item was. They would then count up independent of each other. 
  ''',

  'author':'Odoo PS',

  'website':'https://www.odoo.com',
  
  'version':'14.0.1.0.0',

  'depends':['sale','mrp'],

  "data":[
    'views/product_template_form_inherit.xml',
    'views/mrp_production_views_inherit.xml'
  ],
}
