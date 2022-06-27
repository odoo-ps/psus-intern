# -*- coding: utf-8 -*-

{
    'name': 'Mindesa: Scheduled Action to Confirm RFQs',
    'summary': """Scheduling action to confirm RFQs """,
    'description': """
        Task id: 2879305
        Create a Scheduled Action that will confirm all RFQs into PO given partner_id = Mindesa SAPI de CV (id = 1 in res.partner) and user_id = OdooBot (id = 1 in res.users).
    """,
    'Author' : 'yixi',
    'website' : 'https://www.odoo.com',
    'category' : 'Training',
    'version' : '0.1',
    'depends': ['purchase'],
    'data' : [
        'views/cron.xml'
    ],
    'license': "OPL-1",
    'demo': [],

}