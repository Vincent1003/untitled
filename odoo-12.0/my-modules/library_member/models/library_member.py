from odoo import fields,models

class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    # 通过下方代码模型可以包含mixin的所有字段和方法
    _inherit = ['mail.thread', 'mail.activity.mixin']
    card_number = fields.Char()
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)
     # 使用代理继承，library.member
     # 中嵌入了继承模型res.partner，因此在创建会员记录时，一个关联的
     # Partner
     # 会自动被创建并通过partner_id字段引用。

     # 会员卡模型可使用
     # Partner
     # 中的所有字段，如
     # name, address和
     # email，以及会员自身的独有字段，如card_number

     # 在后台中，Partner
     # 字段存储在关联的
     # Partner
     # 记录，没有重复的数据结构。

     # 对于模型方法则并非如此，Partner
     # 模型中的方法在
     # Member
     # 模型中不可使用。