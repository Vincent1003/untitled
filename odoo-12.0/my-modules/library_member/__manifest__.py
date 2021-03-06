# -*- coding: utf-8 -*-
{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'author': "jy_wang",
    'depends': ['library_app','mail'],
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_view.xml'
    ],
}