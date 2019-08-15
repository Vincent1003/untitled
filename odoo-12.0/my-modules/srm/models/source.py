from odoo import models, fields

class source(models.Model):
    _name = 'srm.source'
    _description = 'srm source'
    name = fields.Char('结算凭证', required=True)
    supplier_id = fields.Many2one('srm.master.supplier', string='供应商', required=True)
    order_id = fields.Many2one('srm.order', string='订单编号', required=True)
    material_id = fields.Many2one('srm.master.material', string='物料', required=True)
    unit = fields.Char('单位')
    quantity = fields.Float(digits=(15, 5), string='数量', required=True)
    tax_rate = fields.Float(digits=(5, 3), string='税率', required=True)
    unit_price = fields.Float(digits=(20, 5), string='单价', required=True)
    pre = fields.Float(digits=(15, 5), string='每', required=True)
    audit_amount = fields.Float(digits=(20, 5), string='金额(不含税)', required=True)
    company_id = fields.Many2one('srm.master.company', string='公司')
    factory_id = fields.Many2one('srm.master.factory', string='工厂')
    warehouse_id = fields.Many2one('srm.master.warehouse', string='仓库', required=True)
    status = fields.Selection([('DRAFT', '未确定'), ('UN_SETTLED', '未结算'), ('SETTLED', '已结算'), ('SETTLED_WITHDRAW', '已取消')], string='状态', required=True)
    source = fields.Selection([('INTERNAL', '内部'), ('EXTERNAL', 'SAP')], string='来源', required=True)




