
from odoo import models, fields, api

class bug(models.Model):
        _name = 'bm.bug'  # 类的唯一标识字段
        _description = 'bug'  # 标签 描述 提高查询友好性
        name = fields.Char('bug简述',required=True)
        detail = fields.Text(size=150)  # 文本字段 用size属性定义长度
        is_closed = fields.Boolean('是否关闭')  # 布尔型
        close_reason = fields.Selection(  [('changed','已修改'),('cannot','无法修改'),('delay','推迟')]   ,string='关闭理由')
        # Selection(list,string ='标签名称')
        user_id = fields.Many2one('res.users',string='负责人')
        follower = fields.Many2many('res.partner',string='关注者')  # 通常用x_id或者者x_ids来区分当前字段是多对一或者一对多
        # 常用属性
        # string 前端显示的名称
        # required 是否必填
        # help 前端显示 作为提示信息
        # index 布尔型 默认False 为真时会在数据库建立索引

        # 保留字段
        # id 记录的唯一标识
        # create_date 记录创建日期
        # create_uid Many2one类型 创建该记录的用户
        # write_date 记录的最后修改日期
        # write_uid 记录最后修改的用户 Many2one类型
        # _last_update 该字段不会实际存储 起到并发检查作用
        # 以上字段可以在前端开发模式下通过debug模式按钮的查看元数据选项查看

        @api.multi
        def do_close(self):
                for item in self:
                        item.is_closed=True
                return True