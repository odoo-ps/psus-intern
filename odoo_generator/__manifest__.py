
{
    'name': 'Odoo Generator',
    'sumary': 'Industrial Kiln & Dryer Group : Job number, Plant code',
    'description': """
        odoo Generator helps to generate the job number and plant code.
    """,
    'author': 'Odoo PS',
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'license': 'OPL-1',
    'data': [
        'views/sale_order_views_inherit.xml',
        'views/res_partner_views_inherit.xml',
    ],
}
