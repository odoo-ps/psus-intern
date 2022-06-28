{
    "name": "greenville",
    "summary": """
        New module for GreenVille
        """,
    "description": """
        New module called product.lists will contain products that users select.
        On the ecommerce website, if current user has product lists selected, he or she can only see
        the products that are inside the product list
    """,
    "author": "odoo",
    "website": "http://www.odoo.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "sale"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/res_partner_inherit.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
}
