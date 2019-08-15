from odoo import models, fields
# 收货单管理
class receive_order(models.Model):
    _name = 'srm.receive.order'
    _description = 'srm receive_order'
    name = fields.Char('收货单号', required=True)  # required必填
    ship_time = fields.Date('收货时间', required=True)
    arrival_time = fields.Date('收货日期', required=True)
    unloading_person = fields.Char('卸货负责人')
    unloading_telephone = fields.Char('卸货口电话')
    delivery_type = fields.Char('交货方式')
    supplier_id = fields.Many2one('srm.master.supplier', string='供应商', required=True)     # 从主数据中的供应商信息获取 required必填
    company_id = fields.Many2one('srm.master.company', string='公司', required=True)
    warehouse_id = fields.Many2one('srm.master.warehouse', string='仓库', required=True)
    receive_from = fields.Char('收货地')
    status = fields.Selection([('DRAFT', '草稿'), ('RELEASED', '已发货'), ('RECEIVED_ALL', '已收货'), ('CANCELLED', '已取消'), ('RECEIVED_PORTION', '部分收货'), ('RETURNED', '已退货'), ('VERIFIED', '已认证'), ('UNVERIFIED', '未认证')], string='状态', required=True)
    remark = fields.Char('备注')

