# -*- coding: utf-8 -*-
{
    'name': "school-v2",

    'summary': """ School module""",

    'description': """School module for testing purposes""",

    'author': "kovorotniy",
    'website': "https://www.github.com/kovorotniy/odoo-school-module",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/teacher_view.xml',
        'views/parent_view.xml',
        'views/student_view.xml'
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
   # 'demo': [
   #     'demo/demo.xml',
   # ],
}