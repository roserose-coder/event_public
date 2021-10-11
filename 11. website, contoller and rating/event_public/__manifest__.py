# -*- coding: utf-8 -*-
{
    'name': "event_public",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'customization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','digest','website'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/views.xml',
        'views/templates.xml',
        'views/form_event.xml',
        'data/event_data.xml',
        'views/res_partner.xml',
        'views/digest.xml',
        'data/cron.xml',
        'views/templates.xml',
        'views/survey_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': -1500
}
