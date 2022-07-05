# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class EDIStatus(models.AbstractModel):
    _name = 'sync.document.status'
    _description = 'EDI Status'

    edi_status = fields.Selection([('pending', 'Pending'), ('sent', 'Sent'),('processed', 'Processed')], string='EDI Status', default='pending', copy=False)
    edi_sync_time = fields.Datetime('EDI Sync Time', copy=False)

    def _execute_edi_sync(self, doc_code, records=False):
        sync_action = self.env['edi.sync.action'].search([('doc_type_id.doc_code', '=', doc_code)], limit=1)
        if not sync_action:
            if self._context.get('ignore_edi_errors', False):
                return True
            raise UserError(_('EDI synchronization action not found'))
        try:
            sync_action.do_doc_sync_user(records=records)
        except Exception as e:
            raise UserError(e)
        return True
