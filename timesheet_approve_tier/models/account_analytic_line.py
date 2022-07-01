from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    validated_status = fields.Selection(selection_add=[
        ('pm', 'Validated by PM'),
        ('manager', 'Validated by Manager'),
        ('validated',),
    ], ondelete={'pm': 'cascade', 'manager': 'cascade'})
    approver_id = fields.Many2one('res.users', 'Approver', readonly=True)

    def create(self, values):
        out = super().create(values)
        for line in out:
            line.approver_id = line.project_id.user_id
            if not line.approver_id:
                line.approver_id, line.validated_status = line._assign_manager_as_approver()
        return out

    def action_validate_timesheet(self):
        if self.user_has_groups('hr_timesheet.group_timesheet_manager,hr_timesheet.group_hr_timesheet_approver'):
            return super().action_validate_timesheet()

        for line in self:
            if line.validated_status == 'draft' or line.validated_status == 'pm':
                approver, step = line.project_id.user_id, 'draft'
                if not approver:
                    approver, step = line._assign_manager_as_approver()
                line.approver_id = approver
                line.validated_status = step

    def _assign_manager_as_approver(self):
        self.ensure_one()
        step = 'pm'
        approver = self.env['hr.employee'].search([
            ('user_id', '=', self.user_id.id)
        ]).user_id
        if not approver:
            step = 'manager'
        return approver, step
