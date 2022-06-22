# -*- coding: utf-8 -*-
{
    'name': "Sync Invoice with Subscription Address",

    'summary': "Copy the Subscription Contact's address to the Invoice on creation",

    'description': """
        Copy the Subscriber's address to the Invoice on creation.

        When a Contact is present on a Subscription, and an invoice is created from that Subscription,
        the delivery address will be copied from the Subscription's Contact.

        Task link:
        https://www.odoo.com/web#id=2874276&menu_id=5200&cids=3&action=4665&active_id=2874261&model=project.task&view_type=form
    """,

    'license': 'OPL-1',

    'author': "Odoo Inc",
    'website': "https://odoo.com",

    'category': 'Custom Development',
    'version': '1.0',
    'application': False,
    'installable': True,
    'auto_install': True,

    'depends': ['sale_subscription'],

    'data': [
        'views/views.xml',
    ],
}
