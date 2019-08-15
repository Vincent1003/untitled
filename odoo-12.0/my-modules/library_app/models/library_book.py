from odoo import api, fields, models
from odoo.exceptions import Warning
# 声明了新的模型，它是models.Model派生出的一个类。然后_name 属性定义
# 了 Odoo 全局对该模型引用的标识符。注意Python 类名 Book 与框架无关，_name
# 的值才是模型的标识符。
class Book(models.Model):
    # 仅有模型名使用点号(.) 来分割关键字，其它如模块、XML
    # 标识符、数据表名等都使用下划线(_)。
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')


    @api.multi
    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-', '') # 为保持兼容性 Alan 自行添加
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a,b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain !=0 else 0
            return digits[-1] == check

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
            return True
        # 模型方法无需返回值，但此处需至少返回True
        # 值。因为不是所有XML - RPC客户端实现都支持
        # None / Null空值，这种情况若返回空值则会导
        # 致抛出错误