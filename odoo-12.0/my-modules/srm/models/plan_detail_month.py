from odoo import models, fields

class planDetailMonth(models.Model):
    _name = 'srm.plan.detail.month'
    _description = 'srm purchase plan month detail'
    name = fields.Char('计划编号', required=True)
    date = fields.Date('计划月份', required=True)
    amount = fields.Integer('所需数量', required=True)
    remark = fields.Char('备注')
    source = fields.Selection([('SAP', 'SAP'), ('INTERNAL', '内部数据')], string='来源', required=True)