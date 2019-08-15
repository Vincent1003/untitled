# -*- coding: utf-8 -*-
{
    'name': "bug管理",

    'summary': """
        这是一个用来测试学习的模块""",

    'description': """
        这是一个用来测试学习的模块
    """,

    'author': "jy_wang",
    'website': "baidu.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
        'views/follower.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}