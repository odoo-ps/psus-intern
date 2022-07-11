{
    'name': 'Many2Many Widgets',
    'version': '1.0',
    'description': 'Extra widgets for Many2Many fields',
    'summary': 'Extra widgets for Many2Many fields',
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Custom Development',
    'depends': [
        'web',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
    'assets': {
        'web.assets_backend': ['m2m_widgets/static/src/*.js'],
    }
}
