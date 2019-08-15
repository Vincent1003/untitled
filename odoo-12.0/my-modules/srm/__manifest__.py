# -*- coding: utf-8 -*-
{
    'name': "SRM",

    'summary': """
        供应商关系管理系统
    """,

    'description': """
        供应商关系管理系统
    """,

    'author': "wisdom",
    'website': "http://www.westinfosoft.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 模块声明中data键所声明文件的顺序非常重要，
        # 因为无法在其它视图或ACL文件中引用还未定义的组
        # 最好将权限数据文件放在ACL文件和其它用户界面数据文件列表的最上面


        # 引入配置权限的csv文件
        'security/ir.model.access.csv',

        'security/srm_security.xml',


        'views/views.xml',
        'views/templates.xml',
        'views/master.xml',
        'views/plan.xml',
        'views/order.xml',
        'views/invoice.xml',
        'views/statement.xml',
        'views/receive_order.xml',
        'views/application_form.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'sequence': 1,
}