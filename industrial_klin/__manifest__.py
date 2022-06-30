{
    'name': 'Industrial Klin',
    'sumary': 'Add job numbers and plant code to the Klin database',
    'description': """
        App to create job numbers and plant code for the Klin database:
        -quotation job number
        -Customer plant code
    """,
    'author': 'Odoo PS',
    'category': 'Serial number',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'license': 'OPL-1',
    'data': [
        'views/sale_view_form_inherit.xml',
        'views/contact_form_inherith.xml',
    ],
}
