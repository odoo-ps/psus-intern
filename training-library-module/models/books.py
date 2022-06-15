# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Books(models.Model):
    _name = 'library.books'
    _description = 'inventory system for books'
    
    title = fields.Char(string='Title', required=True)
    authors = fields.Char(string='Authors',required=True)
    editors = fields.Char(string='Editors',required=True)
    publisher = fields.Char(string='Publisher', required=True)
    ISBN = fields.Integer(string='ISBN', required=True, format=None)
    genre = fields.Selection([
        ('action', 'Action'),
        ('classic', 'Classic'),
        ('detective', 'Detective'),
        ('fantasy', 'Fantasy'),
        ('historical_fiction', 'Historical Fiction'),
        ('non_fiction', 'Non Fiction'),
        ('other', 'Other')
    ])

    active = fields.Boolean(string='Active', default='True')

    @api.onchange('ISBN')
    def _check_ISBN(self):
        if len(str(self.ISBN)) != 13:
            raise ValidationError('ISBN must be exactly 13 digits')


