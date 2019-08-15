from odoo import models, fields

class statementDetail(models.Model):
    _name = 'srm.statement.detail'
    _description = 'statement detail'
    name = fields.Char('凭证号', required=True)
    order_id = fields.Many2one('srm.order', string='订单号', required=True)
    material_id = fields.Many2one('srm.master.material', string='物料名称', required=True)
    unit_price = fields.Float(digits=(20, 5), string='单价', required=True)
    amount = fields.Float(digits=(20, 5), string='金额(含税)', required=True)
    tax_rate = fields.Float(digits=(5, 3), string='税率', required=True)
    tax_amount = fields.Float(digits=(20, 5), string='税额', required=True)
    audit_amount = fields.Float(digits=(20, 5), string='金额(不含税)', required=True)
    unit = fields.Char('单位')
    pre = fields.Float(digits=(15, 5), string='每', required=True)
    warehouse_id = fields.Many2one('srm.master.warehouse', string='仓库', required=True)



