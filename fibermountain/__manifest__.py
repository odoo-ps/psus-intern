{
    'name': 'fiberMountain',
    'summary': """Module copy res parner in invoice""",
    'description': """Add the parner address in the invoce with in the subscription""",
    'author': 'Odoo PS',
    'website':'https://www.odoo.com',
    'category': 'Administrative',
    'version': '14.0.1.0.0',
    'depends': [
        'product',
    ],
    'data':[
        'views/product_template_inherit_cable.xml',
        ],
    'license' : 'OPL-1', 
}
