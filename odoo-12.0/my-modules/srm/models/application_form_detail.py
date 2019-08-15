from odoo import models, fields
class applicationFormDetail(models.Model):
    _name = 'srm.application.form.detail'
    _description = 'application_form detail'
    no = fields.Many2one('srm.application.form', string='编号', required=True)
    applyTime=fields.Date('申请时间',required=True)
    nextApprover = fields.Char('下一审批人',required=True)
    lastApprovTime = fields.Date('上次审批时间')