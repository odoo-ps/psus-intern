# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class EDIStatus(models.AbstractModel):
    _name = 'sync.document.status'
    _description = 'EDI Status'

    edi_status = fields.Selection([('pending', 'Pending'), ('sent', 'Sent'),('processed', 'Processed')], string='EDI Status', default='pending', copy=False)
    edi_sync_time = fields.Datetime('EDI Sync Time', copy=False)

    def _execute_edi_sync(self, doc_code, records=False, raise_user_error=True):
        sync_action = self.env['edi.sync.action'].search([('doc_type_id.doc_code', '=', doc_code)], limit=1)
        if not sync_action:
            if raise_user_error:
                raise UserError(_('EDI synchronization action not found'))
            return True
        try:
            sync_action.do_doc_sync_user(records=records)
        except Exception as e:
            raise UserError(e)
        return True
