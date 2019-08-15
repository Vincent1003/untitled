from odoo import models, fields


class purchase(models.Model):
    _name = 'srm.order'
    _description = 'srm order'
    name = fields.Char('编号', required=True)
    supplier_id = fields.Many2one('srm.master.supplier', string='供应商')
    type = fields.Selection([('CONVENTIONAL', '常规订单')], string='类型', required=True)
    company_id = fields.Many2one('srm.master.company', string='公司名称')
    status = fields.Selection([('DRAFT', '草稿'), ('RELEASED', '已发布'), ('CONFIRMED', '已确认'), ('CANCELLED', '已取消'), ('CLOSED', '已关闭'), ('INVOICED', '已发货')], string='状态', required=True)