#-*- encoding: utf-8 -*-

from odoo import tools, models, fields, api, _
from odoo.exceptions import AccessError
class ModifiedAnalyticLine(models.Model):
    _inherit='account.analytic.line'


    current_level = fields.Selection(selection = [
                                      ('1', 'timesheet_access_levels.group_access_levels_pm'),
                                      ('2', 'timesheet_access_levels.group_access_levels_supervisor'),
                                      ('3', 'timesheet_access_levels.group_access_levels_admin'),
                                      ], default='1',string="Needs approval from")

    user_can_validate = fields.Boolean(compute='_compute_can_validate',
        help="Whether or not the current user can validate/reset to draft the record.")

    invoice_ready = fields.Boolean(required=True, default=False)

    levels_of_approval = fields.Integer(default=3)

    

    def _compute_can_validate(self):
        print('validate function overwritten')
        curr_permitted_editor = dict(self._fields['current_level'].selection).get(self.current_level)
        for line in self:
            if (self.env.user.has_group(curr_permitted_editor) and (
                not curr_permitted_editor == 'access-levels.group_access_levels_pm' or 
                line.employee_id.timesheet_manager_id.id == self.env.user.id)):
                    line.user_can_validate = True
            else:
                line.user_can_validate = False
    
    @api.depends('user_can_validate') 
    def write(self, vals):
        currLevelIntValue = int(self.current_level)       
        if self.user_can_validate or currLevelIntValue == 1:
            res = super(ModifiedAnalyticLine, self).write(vals)
            return res
        else:
            raise AccessError(_('You are attempting to edit a timesheet you do not have access to'))
            


    @api.depends('user_can_validate')
    def action_validate_timesheet(self):
        for record in self:
            currLevelIntValue = int(record.current_level)
            if record.user_can_validate:
                if currLevelIntValue < record.levels_of_approval: 
                    record.current_level = str(currLevelIntValue + 1)
                else:
                    record.invoice_ready = True
            else:
                raise AccessError(_("You are trying to validate a timesheet that you do not have permission to"))


    @api.depends('user_can_validate')
    def action_invalidate_timesheet(self):
        for record in self:
            if record.user_can_validate: 
                record.current_level = '1'
                invalidator_id = record.env.user.partner_id.id
                message_text=_('Your timesheet was invalidated. Please review and resubmit it.')

                channel = record.env['mail.channel'].with_context(mail_create_nosubscribe=True).sudo().create({
                    'channel_partner_ids': [(4, record.create_uid.partner_id.id)],
                    'public': 'private',
                    'channel_type': 'chat',
                    'name': f'Timesheet Invalidated',
                    'display_name': f'Timesheet Invalidated',
                })

                channel.sudo().message_post(
                    body=message_text,
                    author_id=invalidator_id,
                    message_type="comment",
                )

            else:
                raise AccessError(_("You are trying to invalidate a timesheet that you do not have permission to"))

