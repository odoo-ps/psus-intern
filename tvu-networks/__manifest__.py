# -*- coding: utf-8 -*-
{
    'name': 'TVU Networks: Auto-Cancel Quotations',
    'summary': """Automated action to remove the expired quotations""",
    'description': """To allow for more accurate sales reporting without creating extra administrative work, we would like to automatically cancel quotations 
                    which are no longer relevant, as defined by the quotation passing its expiration date.
                    Task Id: 2874198""",
    'author': 'Odoo Inc',
    'website': 'https://www.odoo.com',
    'category':'Training',
    'version':'1.0',
    'depends': ['sale'],
    'data':[         
        'data/sales_view_order.xml'
    ], 

}