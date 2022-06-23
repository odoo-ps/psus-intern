{
    "name": "OWL Framework",
    "summary": """ """,
    "description": """
        Carniceria Paredes module:
        Add seletion field of customer type on client screen
        Developer: damu
    """,
    "author": "Odoo",
    "website": "https://www.odoo.com",
    "category": "Custom Development",
    "version": "15.0.1.0.0",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        'views/res_partner_inherit_views.xml'],
    "assets": {
        'point_of_sale.assets': [
            'owl_framework/static/src/js/OWLClientDetailsEdit.js',
        ],
        "web.assets_qweb": [
            "owl_framework/static/src/xml/ClientDetailsEdit.xml",
        ],
    },
    "license": "OPL-1",
}
