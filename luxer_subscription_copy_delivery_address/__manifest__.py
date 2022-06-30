{
    'name': 'Copy Property to Invoice',
    'version': '15.0.1.0.0',
    'summary': 'Automatically copy res.partner property to invoice',
    'category': 'Sales',
    'author': 'Odoo',
    'website': 'https://odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'sale_subscription',
        'account',
    ],
    'data': [
        'views/sale_subscription_inherit.xml',
        'views/invoice_subscription_inherit.xml',
    ],
}

