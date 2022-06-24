# -*- coding: utf-8 -*-

{
    'name': 'Odoo Access Rights',
    'summary': """FGD Glass Solutions: Access rights changes""",
    'description': """
        Access rights module to manage the access rights of the users:
        Sales/all group after creating a new user they cannot will be able to change the sales person o pricelist of them

    """,
    'author': 'Odoo-psus',
    'website': 'https://www.odoo.com',
    'category': 'Contact',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'views/res_partner_inherit.xml',
        'security/ir.model.access.csv',
    ]
}
