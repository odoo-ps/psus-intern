{
    'name': 'Documentation',
    'version': '1.0',
    'summary': 'Odoo documentation',
    'description': """
        Odoo codebase documentation.
        For internal use only.

        Uses PDoc internally; specs can be configured in Settings.
        """,
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Documentation',
    'depends': ['base'],
    'external_dependencies': {
        'python': ['pdoc'],
    },
    'data': [
        'views/views.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
