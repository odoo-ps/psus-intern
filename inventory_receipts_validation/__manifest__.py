# -*- coding: utf-8 -*-
{
    'name': "Validate Warehouse Receipts",

    'license': 'OPL-1',

    'summary': "Validate that warehouse receipts don't receive more than demanded.",

    'description': """
        Validate that warehouse receipts don't receive more than demanded.

        The check is performed only when editing receipts.

        Task link:
        https://www.odoo.com/web#id=2874272&menu_id=5200&cids=3&action=4665&active_id=2874261&model=project.task&view_type=form
    """,

    'author': "Odoo Inc",
    'website': "https://odoo.com",

    'category': 'Custom Development',
    'version': '1.0',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['stock'],
}
