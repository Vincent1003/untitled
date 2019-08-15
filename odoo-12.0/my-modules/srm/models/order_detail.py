from odoo import models, fields

class orderDetail(models.Model):
    _name = 'srm.order.detail'
    _description = 'order detail'
    order_id = fields.Many2one('srm.order', string='订单编号', required=True)
    line_code = fields.Char('行号', required=True)
    material_id = fields.Many2one('srm.master.material', string='物料名称', required=True)
    requested_arrival_date = fields.Date('要求到货日期')
    required_quantity = fields.Integer('需求数量')
    can_send_quantity = fields.Integer('可发数量')
    send_quantity = fields.Integer('已发数量')
    receive_quantity = fields.Integer('已收数量')
    return_quantity = fields.Integer('退货数量')
    unit = fields.Char('单位')
    factory_id = fields.Many2one('srm.master.factory', string='工厂', required=True)
    warehouse_id = fields.Many2one('srm.master.warehouse', string='仓库', required=True)
    status = fields.Selection([('NORMAL', '正常'), ('EDITED', '已修改'), ('CANCELLED', '已取消'), ('CLOSE', '已关闭')], string='状态', required=True)

