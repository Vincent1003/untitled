from odoo import models, fields

class plan(models.Model):
    _name = 'srm.plan'
    _description = 'srm purchase plan'
    name = fields.Char('计划名称', required=True)
    company_id = fields.Many2one('srm.master.company', string='公司', required=True)
    factory_id = fields.Many2one('srm.master.factory', string='工厂', required=True)
    material_id = fields.Many2one('srm.master.material', string='物料', required=True)
    supplier_id = fields.Many2one('srm.master.supplier', string='供应商', required=True)
    purgroup_id = fields.Many2one('srm.master.purchasegroup', string='采购组', required=True)
    unit = fields.Char('单位')
    status = fields.Selection([('PUBLISHED', '已发布'), ('UNPUBLISHED', '未发布')], string='发布状态', required=True)
    remark = fields.Char('备注')
    source = fields.Selection([('SAP', 'SAP'), ('INTERNAL', '内部数据')], string='来源', required=True)