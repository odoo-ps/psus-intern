# -*- coding: utf-8 -*-

{
    'name': 'Job number / Plant Code',
    'version': '15.0.0.1',
    'category': 'sales',
    'summary': 'Creator of job number/plant codes when filling out a new quotation.',
    'description': """
Job Number / Plant Code
=======================
Job Number / Plant Code fields for sales orders
using sequencing numbers upon creation 
of a quotation/sale order
Author: yall
task: 2874544
    """,
    'depends': [
        'sale',
    ],
    'author': 'Odoo PS',
    'data': [
        'views/sale_order_view_inherit.xml',
        'data/job_number_sequence.xml',
        'data/plant_number_sequence.xml',
    ],
    'demo': [
    ],
    'license': 'OPL-1',
}
