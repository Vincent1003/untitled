from odoo import http
from odoo.addons.library_app.controllers.main import Books

class BookExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get('available'):
            Book = http.request.env['library.book']
            books = Book.search([('is_available', '=', True)])
            response.qcontext['books'] = books
        return response

    # 这和模型不同，模型可以通过
    # env
    # 对象中的central
    # registry
    # 来引用任意模型类，而无需了解实现它的文件。
    # 控制器没有这个，我们需要知道实现需继承控制器的模块和文件。

    # 基于Books声明了一个BooksExtended类，类名不具关联性，
    # 仅用于继承和扩展原类中定义的方法。

    # 定义了一个控制器方法
    # list()。它至少需要一个简单的 @ http.route()
    # 装饰器来保持路径活跃。如果不带参数，将会保留父类中定义的路由。但也可以为 @ http.route()
    # 装饰器添加参数，来重新定义或替换类路由。