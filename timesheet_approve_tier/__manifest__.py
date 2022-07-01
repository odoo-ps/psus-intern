# -*- coding: utf-8 -*-
{
    'name': "Timesheet Approve Tier",

    'summary': 'Require timesheet approval from PM and Manager',

    'description': """
        Require timesheet approval from PM and Manager.

        Adds a new group: "User: assigned timesheets". Users in this group (i.e. PMs and managers)
        can approve timesheets assigned to them. Only when both approvals are cleared will
        the timesheet be sent to the general timesheet manager.

        This also disallows timesheet managers from approving timesheets without the dual approval,
        but timesheet administrators maintain their ability to approve any timesheet.

        Task ID: 2874281
    """,

    'author': "Odoo Inc",
    'website': "https://www.odoo.com",

    'category': 'Custom Development',
    'version': '1.0',

    'depends': ['timesheet_grid'],

    'data': [
        'security/rules.xml'
    ],
}
