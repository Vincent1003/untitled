# -*- coding: utf-8 -*-
{
    'name': "library management",
    'summary': """manage library book catalogue and lending""",
    'description':"""manage library book catalogue and lending""",
    'author': "jy_wang",
    'website':"www.baidu.com",
    'application': True,
    'sequence': 2,
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
        'security/library_security.xml',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}