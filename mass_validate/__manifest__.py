# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Mass Timesheet Validation Button",
    'summary': """Assigns access levels when validate button is used""",
    'description': """
        Timesheets are subject to 3 stages of approval, from the
        project leader, project manager, and then the timesheet
        approver. Each approver will be able to mass validate the
        given timesheets in tree view when it is submitted to them
        consecutively. Once the timesheets are approved by all
        three approvers, only then can it be processed for invoicing.

        This process works for employee timesheets as well as expense
        report submissions.

        Task ID: 2873674
        """,
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OPL-1',
    # any module necessary for this one to work correctly
    'depends': ['hr_timesheet',
                'hr_expense'],
    'application': False,
    'auto_install': False
}
