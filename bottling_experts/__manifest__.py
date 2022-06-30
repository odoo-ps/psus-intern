{
    'name': '',
    'sumary': ' Product Lists Module ',
    'description': """
        Module to add product lists for eCommerce website
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
        'mrp'
    ],
    'data': [
        'report/bottling_experts_report.xml',
        'views/sale_order_views_inherit.xml',
    ],
    'assets':{
        'web.assets_common': [
            'bottling_experts/static/src/css/report.css',
        ],
    },
    'license': 'OPL-1',
}
