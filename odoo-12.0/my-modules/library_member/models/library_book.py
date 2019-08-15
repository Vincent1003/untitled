from odoo import fields,models

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