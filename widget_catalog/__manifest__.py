{
    'name': 'Widget Catalog',
    'version': '1.0',
    'description': 'Widget Catalog',
    'summary': 'Widget Catalog',
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com/',
    'license': 'OPL-1',
    'category': 'Documentation',
    'depends': [
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_qweb': [
            'widget_catalog/static/src/xml/preview.xml'
        ],
        'web.assets_backend': [
            'widget_catalog/static/src/preview.js'
        ],
    }
}
