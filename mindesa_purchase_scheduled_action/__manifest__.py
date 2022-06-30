# -*- coding: utf-8 -*-
{
    'name': "Mindesa Purchase Scheduled Action",

    'summary': """Automatically transfer RFQ to PO of Mindesa""",

    'description': """
        [Automatically create a Scheduled Action that will confirm all RFQs into PO given partner_id = Mindesa SAPI de CV (id = 1 in res.partner) and user_id = OdooBot (id = 1 in res.users).]
        """,

    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
