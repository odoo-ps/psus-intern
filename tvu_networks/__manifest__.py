# -*- coding: utf-8 -*-

{
    'name': "TVU Networks: Auto-cancel expired quotations",
    'summary': """
        auto-cancel expired quotations
    """,
    'description': """
        task_id: 2874339
        Added a scheduled action and '_remove_expired_quotations' method to sale.order to auto-cancel expired quotations
    """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'application': False,
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['sale'],
    'data': [
        'data/ir_cron_data.xml'
    ]
}
