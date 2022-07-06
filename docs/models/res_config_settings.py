from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pdoc_specs = fields.Char('PDoc Specs',
                             default='odoo,!odoo.addons.test*,!odoo.addons.l10n*',
                             config_parameter='docs.pdoc_specs',
                             help="""
        Comma-separated list of modules to include in the documentation.
        Patterns beginning with a ! will exclude matching modules. For example,
        `odoo,!odoo` will only document the `odoo` module itself, but not its submodules.
        """)
