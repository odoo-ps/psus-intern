# -*- coding:utf-8 -*-

{
    'name':"TVU Networks: Auto-Cancel Expired Quotations",
    'summary':"""an App to auto-cancel the expired quotations at midnight""",
    'description':"""
       TVU Networks: Auto-Cancel Expired Quotations
       -The module add an function to trigger the calcel action for expired quotations
        at midnight
       -Task ID:2874376 
    """,
    'author':'Odoo Inc',
    'website': 'https://www.odoo.com',
    'category':'Custom Development',
    'version':'15.0.1.0',
    'license':'OPL-1',
    'depends':['sale'],
    
    'data':[
        'views/inventory_menuitems.xml',
        'security/management_security.xml',
        'security/ir.model.access.csv',
        'views/products_views.xml',
        'views/product_template_view_inherit.xml'  
    ] 
}
