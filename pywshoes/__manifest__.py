# -*- coding: utf-8 -*-
{
    'name': 'NY P&W Shoes',
    'summary': """Auto-calculated price""",
    'description': """NY P&W Shoes is a shoe distributor in New York. They buy shoes in large quantities from China and redistribute them here in the US. [romf]""",
    'author': 'Odoo PS',
    'website':'https://www.odoo.com',
    'category': 'Administrative',
    'version': '15.0.1.0.0',
    'depends': [
        'sale',
        'product',
    ],
    'data':[
        'views/product_template_inherit.xml',
        ],
    'license' : 'OPL-1',
}
