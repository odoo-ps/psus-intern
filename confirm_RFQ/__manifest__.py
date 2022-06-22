# -*- coding: utf-8 -*-

{
    'name': 'Confirm RFQ with scheduled action.',
    'summary': """Module to confirm all RFQ's made by the customer every day.""",
    'description': """
        We need to check for the partner_id to be == 1 and the user_id to be == 1.
        If this is the case, confirm the RFQ to be a PO. 
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '15.0.1.0.0',
    'depends': ['purchase'],
    'license': 'OPL-1',
}
