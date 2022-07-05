# -*- coding: utf-8 -*-
{
    "name": "3PL Central EDI: Inventory",
    "summary": """Implement EDI integration with 3PL Central""",
    "description": """
Allows Importing and Exporting EDI Purchase Orders to 3PL Central
=================================================================

This module implements the following EDI document types to communicate 
with 3PL Central.

- 846 - Inventory Advice
- 940 - Shipping Order
- 943 - Shipment Advice
- 944 - Receipt Advice
- 945 - Shipping Advice    
    """,
    "author": "Odoo Inc",
    "website": "https://www.odoo.com/",
    "category": "Tools",
    "version": "14.0.1.0.0",
    "license": "OPL-1",
    "depends": ["base_edi","stock","delivery"],
    "data": [
        "data/edi_sync_data.xml",
        "data/picking_actions.xml",
        "data/ir_cron.xml",
        "views/940_edi_template.xml", 
        "views/943_edi_template.xml",
        'views/delivery_carrier_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_location_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml'
    ],
    "application": False,
}
