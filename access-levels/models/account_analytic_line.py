#-*- encoding: utf-8 -*-

from odoo import tools, models, fields, api, _
from odoo.exceptions import AccessError
class ModifiedAnalyticLine(models.Model):
    _inherit='account.analytic.line'
    _description='modifed anayltic acocunt line'

    #use built in methods to valid and invalidate timesheets
    #ping specific user when time is right


    current_level = fields.Selection(selection = [
                                      ('1', 'access-levels.group_access_levels_pm'),
                                      ('2', 'access-levels.group_access_levels_supervisor'),
                                      ('3', 'access-levels.group_access_levels_admin'),
                                      ], default='1')

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
    def action_validate_timesheet(self):
        currLevelIntValue = int(self.current_level)
        if self.user_can_validate:
            if currLevelIntValue < self.levels_of_approval: 
                self.current_level = str(currLevelIntValue + 1)
            else:
                self.invoice_ready = True
        else:
            raise AccessError(_("You are trying to validate a timesheet that you do not have permission to"))


    @api.depends('user_can_validate')
    def action_invalidate_timesheet(self):
        currLevelIntValue = int(self.current_level)
        if self.user_can_validate and currLevelIntValue >= 1: 
            self.current_level = str(currLevelIntValue - 1)
            people_to_notify = [self.create_uid]
            if self.current_level == '2':
                people_to_notify.append(self.employee_id.timesheet_manager_id.id)
            self.message_post(body="A timesheet that you approved was invalidated. Please review it.", partner_ids=[(6,self.create_uid)])
        else:
            raise AccessError(_("You are trying to invalidate a timesheet that you do not have permission to"))