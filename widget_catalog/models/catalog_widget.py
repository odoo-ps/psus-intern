from odoo import models, fields, api


class CatalogWidget(models.Model):
    _name = 'catalog.widget'
    _description = 'Catalog Widget'

    name = fields.Char(string='Name', required=True)
    type = fields.Selection([
        ('many2one', 'Many2One'),
        ('many2many', 'Many2Many'),
        ('one2many', 'One2Many'),
        ('char', 'Char'),
        ('text', 'Text'),
        ('selection', 'Selection'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('binary', 'Binary'),
        ('datetime', 'Datetime'),
        ('date', 'Date'),
    ], string='Type', required=True, default='char')
    description = fields.Html(string='Description')
    summary = fields.Char(string='Summary')
    example = fields.Html(string='Example')
    module = fields.Char(string='Module')
    parameters = fields.One2many('catalog.widget.parameter', 'widget_id', string='Parameters')

    sample_many2one = fields.Many2one('res.partner', string='Sample Many2One')
    sample_many2many = fields.Many2many('res.partner', string='Sample Many2Many')
    sample_one2many = fields.Many2many('catalog.widget.sample_line', string='Sample One2Many')
    sample_char = fields.Char(string='Sample Char')
    sample_text = fields.Text(string='Sample Text')
    sample_selection = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string='Sample Selection')
    sample_integer = fields.Integer(string='Sample Integer')
    sample_float = fields.Float(string='Sample Float')
    sample_binary = fields.Binary(string='Sample Binary')
    sample_boolean = fields.Boolean(string='Sample Boolean')
    sample_datetime = fields.Datetime(string='Sample Datetime')
    sample_date = fields.Date(string='Sample Date')

    example_field = fields.Char(string='Example Field',
                                compute='_compute_example_field')

    @api.depends('type')
    def _compute_example_field(self):
        for fields in self:
            self.example_field = 'sample_' + fields.type


class CatalogWidgetParameter(models.Model):
    _name = 'catalog.widget.parameter'
    _description = 'Catalog Widget Parameter'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    widget_id = fields.Many2one('catalog.widget', string='Widget', required=True, ondelete='cascade')
    relation_id = fields.Many2one('ir.model.fields', string='Relation', domain=[('type', '=', 'many2one')])


class CatalogWidgetSampleLine(models.Model):
    _name = 'catalog.widget.sample_line'
    _description = 'Catalog Widget Sample Line'

    name = fields.Char(string='Name', required=True)
    value = fields.Char(string='Value', required=True)
    happy = fields.Boolean(string='Happy')
