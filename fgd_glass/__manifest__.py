# -*- encoding: utf-8 -*-

{
    'name': 'FGD Glass Field Access Rights',
    'version': '1.0',
    'author': 'Odoo Inc',
    'summary': 'Module to modify behavior of res.partner model to fit FGD_Glass requirements',
    'description': """This module affects the salesperson and pricelist fields in the res.partner model.  It prevents 
    FGD salespeople from editing the saleslist after a contact has been created. It also forces the salesperson to be the person 
    who created the contact. FGD admins can edit both of these fields at will.""",
    'category': 'Training',
    'license': 'OPL-1',
    'depends':['base','sale'],
    'data':[
        'security/fgd_glass_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml'
    ],
}