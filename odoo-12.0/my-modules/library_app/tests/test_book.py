from odoo.tests.common import TransactionCase

# 创建一本新书并检查active字段的值是否正确
class TestBook(TransactionCase):
    # 第一条命令调用了父类中的setUp代码，下面一条修改了用于测试的环境self.env
    # 为使用admin用户的新环境。
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['library.book']
        self.book_ode = self.Book.create({
            'name': 'Odoo Development Essentials',
            'isbn': '879-1-78439-279-6'})
        return result

    def test_create(self):
        "Test Books are active by default"
        self.assertEqual(self.book_ode.active,True)
        # 测试业务逻辑
        def test_check_isbn(self):
                "Check valid ISBN"
                self.assertTrue(self.book_ode._check_isbn)


    # 测试安全权限
