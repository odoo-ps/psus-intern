# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Copy Property from Subscription to Invoice",
    'summary': "Automatically fills the delivery address from subscription",
    'description': """
        Using the contact record of a property partner on a subscription,
        the address associated with the contact will be copied over to the
        delivery address upon creation of an invoice. If it is blank, it
        will follow normal behavior.

        Task ID: 2873669
    """,
    'author': "Odoo Inc.",
    'website': "https://www.odoo.com/",
    'category': 'Sales',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'sale_subscription',
        'account'],
    'data': [
        'data/sale_subscription_views_inherit.xml',
        'data/invoice_form_views_inherit.xml'
    ],
    'application': False,
    'auto_install': True
}
