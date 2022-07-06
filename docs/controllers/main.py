
from odoo import http, _
from functools import lru_cache
from pdoc import render, extract, web
import traceback
import logging


_logger = logging.getLogger(__name__)


class MainController(http.Controller):
    def __init__(self):
        super().__init__()
        _logger.info('MainController starting')
        self.spec = http.request.env['ir.config_parameter'].sudo().get_param(
            'docs.pdoc_specs', 'odoo,!odoo.addons.test*,!odoo.addons.l10n*,werkzeug')
        render.configure(
            favicon='/web/image/res.company/1/favicon',
            logo='/logo.png',
        )
        self._walk_spec()

    def _walk_spec(self):
        module_paths = extract.walk_specs(self.spec.split(','))
        self.all_modules = web.AllModules(module_paths)

    def _should_revalidate_spec(self):
        spec = http.request.env['ir.config_parameter'].sudo().get_param(
            'docs.pdoc_specs')
        if spec and self.spec != spec:
            _logger.info('New spec: ' + spec)
            self.spec = spec
            self._walk_spec()

    @http.route('/docs/search.js', auth='user')
    def search_index(self):
        try:
            return http.Response(render.search_index(self.all_modules),
                                 mimetype='application/javascript')
        except Exception as err:
            _logger.error(f'{err}:\n{traceback.format_exc()}')
            return http.Response(status=500)

    @http.route('/docs/<path:page>', auth='user', website=True)
    @lru_cache(maxsize=1000)
    def module(self, page):
        self._should_revalidate_spec()
        try:
            path = page.replace('.html', '').replace('/', '.')
            return render.html_module(self.all_modules[path], self.all_modules)
        except KeyError:
            return http.request.not_found(_('Module %s not found.', path))
        except Exception as err:
            _logger.error(err)
            return render.html_error(str(err), traceback.format_exc())

    @http.route('/docs/index.html', auth='user', website=True)
    def index(self):
        self._should_revalidate_spec()
        return render.html_index(self.all_modules)
