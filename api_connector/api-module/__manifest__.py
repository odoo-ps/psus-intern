{
    'name': 'Generic API Connector',
    'summary': """Module to make an API connection using automated actions.""",
    'description': """
        This module will add an option in the automated actions state menu, this option will let the user connect to an API.
        There will be fields that the user needs to fill like authtoken and url for example and the model will convert those inputs into the params
            that the API call will send.
        
        Developers: [gecm], [romf], [ayhp]
        Task ID: 2856455
        Link to project: https://www.odoo.com/web#id=2856455&menu_id=4720&cids=17&action=333&active_id=6182&model=project.task&view_type=form
    """,
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'category': 'Tools',
    'version': '15.0.1.0.0',
    'depends': [
        'base_automation', 
    ],
    'data': [
        #Cron
        'data/clear_logs_cron.xml',
        
        #Views
        'views/view_base_automation_inherit.xml',
        'views/api_views.xml',
        'views/view_server_action_inherit.xml',
        'views/logs_menu_item.xml',

        
        #Security
        'security/ir.model.access.csv',
    ],
    'license': 'OPL-1',
}
