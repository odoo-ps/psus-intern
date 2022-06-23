{
    "name": "OWL Framework",
    "description": """
        OWL Framework module:
        Add selection field of customer type on client edit details view in POS web app
        Developer: damu
    """,
    "author": "Odoo",
    "website": "https://www.odoo.com",
    "category": "POS",
    "version": "15.0.1.0.0",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        'views/res_partner_inherit_views.xml'
    ],
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
