# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Compatibility Filter",
    'summary': """Lists products compatible with the selection.""",
    'description': """
        Filters items that are compatible with the product the
        customer is buying parts for.

        Task ID: 2869113
        """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/filter_views.xml',
        'views/filter_menus.xml',
        'wizard/filter_wizard_views.xml'],
    'application': True,
    'installable': True,
    'auto_install': False
}
