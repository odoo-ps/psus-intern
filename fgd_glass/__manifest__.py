# -*- encoding: utf-8 -*-

{
    'name': 'FGD Glass',
    'version': '1.0',
    'author': 'Justin Deng (jden)',
    'descripton': 'Module to modify behavior of res.partner model to fit FGD_Glass requirements',
    'category': 'Training',
    'license': 'OPL-1',
    'depends':['base','sale'],
    'data':[
        'security/fgd_glass_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml'
    ],
    'demo':[],
}