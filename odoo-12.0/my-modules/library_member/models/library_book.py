from odoo import fields,models,api

class Book(models.Model):
     _inherit = 'library.book'
     is_available = fields.Boolean('Is Available?')
     isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
     publisher_id = fields.Many2one(index=True)

     # 原型(prototype)继承
     # 如在使用_inherit属性的同时还使用了与父模型不同的_name属性
     # 此时会复用所继承并创建一个新的模型，并带有自己的数据表和数据
     # 代理(delegation)继承
     # 通过_inherits属性来使用(注意最后有一个s)。这允许我们创建一个包
     # 含和继承已有模型的新模型。新模型创建新记录时，在原模型中也会被
     # 创建并使用manytoone字段关联。查看新模型的人可以看到所有原模型
     # 和新模型中的字段，但在后台两个模型分别处理各自的数据。

     @api.multi
     def _check_isbn(self):
          self.ensure_one()
          isbn = self.isbn.replace('-', '')
          digits = [int(x) for x in isbn if x.isdigit()]
          if len(digits) == 10:
               ponderators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
               total = sum(a * b for a, b in zip(digits[:9], ponderators))
               check = total % 11
               return digits[-1] == check
          else:
               return super()._check_isbn()

# 要继承方法，我们要重新定义该方法，可以使用 super()来调用已实现的部分。
# 在这个方法中我们验证是否为10位数 ISBN，然后插入遗失的验证逻辑。若不是
# 10位，则进入原有的13位验证逻辑。如果想要进行测试甚至是书写测试用例，可
# 使用0-571-05686-5作为例子，该书是威廉·戈尔丁的《蝇王》。