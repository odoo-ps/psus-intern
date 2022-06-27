{
    'name': 'Greenville Produce',
    'summary': """Unique product lists per customer on website""",
    'description': """Add the parner address in the invoce with in the subscription""",
    'author': 'Odoo PS',
    'website':'https://www.odoo.com',
    'category': 'Administrative',
    'version': '14.0.1.0.0',
    'depends': ['sale','website'],
    'data':[
        'views/product_list_menu_item.xml',
        'views/product_list_view.xml',
        'views/res_partner_inherit.xml',
        'security/product_list_security.xml',
        'security/ir.model.access.csv',
        ],
    'license' : 'OPL-1', 
}
