# -*- coding: utf-8 -*-

# 第一步我们来创建一个显示有效图书列表的简单网页。
# 在请求http://<my-server>/library/books页面时会进
# 行响应，所以/library/books是用于实施的 URL
from odoo import http

class Books(http.Controller):

    @http.route('/library/books', auth='user')
    def list(self, **kwargs):
        Book = http.request.env['library.book']  # 使用http.request.env获取环境，使用它可从目录中获取有效图书记录集
        books = Book.search([])
        return http.request.render(
            'library_app.book_list_template', {'books':books})
        #使用http.request.render() 来处理 library_app.index_template Qweb
        # 模板并生成输出 HTML。可通过字典向模板传值，这里传递了图书记录集。












# class LibraryApp(http.Controller):
#     @http.route('/library_app/library_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_app/library_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_app.listing', {
#             'root': '/library_app/library_app',
#             'objects': http.request.env['library_app.library_app'].search([]),
#         })

#     @http.route('/library_app/library_app/objects/<model("library_app.library_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_app.object', {
#             'object': obj
#         })