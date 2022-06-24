#-*- coding: utf-8 -*-
{
    'name':"Materiales Castelar: Warehouse Control Receipt",
    
    'summary':"""a module to control receipts to make sure the  make sure the different warehouses won't receive more than the ordered quantity """,
    
    'description':"""
       Materiales Castelar: Warehouse Control Receipt
       -Create an action to control the Receipt in Inventory App to make sure the ordered quantity will not greater than the demand for warehouse.
       -Task ID:2874379    
    """,
    
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'category':'Custom Development',
    'version':'15.0.2.0',
    'license': 'OPL-1', 
    'depends':['stock','sale'],
    
    'data':[
        
    ],
    'demo':[
        
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}
