# -*- coding: utf-8 -*-

from odoo import models, fields

class Books(models.Model):
    _name = 'library.books'
    _description = 'inventory system for books'
    
    title = fields.Char(string='Title', required=True)
    authors = fields.Char(string='Authors',required=True)
    editors = fields.Char(string='Editors',required=True)
    publisher = fields.Char(string="Publisher", required=True)
    ISBN = fields.Float(string="ISBN", required=True)
    genre = fields.Selection([
        ('action', 'Action'),
        ('classic', 'Classic'),
        ('detective', 'Detective'),
        ('fantasy', 'Fantasy'),
        ('historical_fiction', 'Historical Fiction'),
        ('non_fiction', 'Non Fiction')
        ('other', 'Other')
    ])
