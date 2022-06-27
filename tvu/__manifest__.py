# -*- coding: utf-8 -*-

{
    "name" : "TVU - Auto-cancel expired orders",

    "summary" : "TVU module to auto-cancel expired orders",

    "description" : "Adds a scheduled function to run every night at midnight (EST) to find orders whose expiration date has passed and changes their state to cancelled",
    
    "author": "Sam Struble",

    "category":"TVU",

    "version":"1.0",

    "license":"LGPL-3",

    "depends" : ["sale"],

    "auto-install":False,

    "installable":True,

    "application":False,

    "data" : [
        "views/sale_views_inherit.xml",
        "data/sale_order_data.xml"
    ],

    "demo" : []

}
