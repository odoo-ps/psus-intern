{
    'name': 'Greenvile Produce Lists',
    'version': '1.0',
    'license': 'OPL-1',
    'author': 'Odoo Inc',
    'category': 'Training',
    'summary': 'Greenvile Produce Training excercise',
    'description': """
        Task ID: 2873831
        Create lists of products to purchase for a customer.
        Only one list per customer.
        Customers can only see their own lists.
    """,
    'depends': ['sale', 'website_sale', 'product'],
    'data': [
        'security/greenvile_security.xml',
        'views/greenvile_menu_items.xml',
        'views/greenvile_product_list.xml',
        'views/res_partner_views.xml',
    ],
}