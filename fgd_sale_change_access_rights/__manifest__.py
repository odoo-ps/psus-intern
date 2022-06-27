# -*- coding: utf-8 -*-
{
    'name': "FGD Sale Change Access Rights",

    'summary': """Change sales person access to make only sale admin to edit it again""",

    'description': """
        [Users of the group sales/own documents only and sales/all documents can enter the value of sales person and pricelist when they create a contact. After creation, if they edit an existing contact, both the salesperson and the sales pricelist field should be read only for them. Users of the group Sales/Administrator and sales/Administrator (commissions) can edit values of the sales person and sales pricelist while creation or editing the res.partner record.]
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        "views/res_partner_inherit.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
