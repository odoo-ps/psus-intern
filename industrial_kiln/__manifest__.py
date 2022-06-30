{
    'name': 'Industrial Kiln & Dryer Group : Job number, Plant code',
    'summary': """Module to create two custom fields and generate them automatically.""",
    'description': """
        There are two fields that need to be created. 
        The first one is Job Number and it belongs in sale.order:
            Job Number is concatenated out of three different fields: 
                -Prefix (selection field).
                -Sequence: predefined sequence that we can specify and edit if required (starts with 13500, eg. 13500, next job number is 13501 and etc)
                -Suffix (selection field).
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_order_views_inherit.xml',
        'views/res_partner_views_inherit.xml',
    ],
    'license': 'OPL-1',
}
