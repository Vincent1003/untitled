from odoo import models, fields

class statement(models.Model):
    _name = 'srm.statement'
    _description = 'srm statement'
    name = fields.Char('结算单号', required=True)
    supplier_id = fields.Many2one('srm.master.supplier', string='供应商', required=True)
    company_id = fields.Many2one('srm.master.company', string='公司', required=True)
    bill_amount = fields.Float(digits=(20, 5), string='总金额(含税)', required=True)
    deliver_type = fields.Char('物流公司')
    deliver_code = fields.Char('物流编号')
    factory_id = fields.Many2one('srm.master.factory', string='工厂')
    status = fields.Selection(
        [('DRAFT', '草稿'), ('RELEASED', '开票审批中'), ('CANCELLED', '已取消'), ('CLOSED', '已关闭'), ('BUYERAPPROVAL', '采购审批'),
         ('INVOICED', '待录入发票'), ('FINANCIALAPPROVAL', '财务审批')], string='状态', required=True)
    send_sap = fields.Selection([('UN_SEND', '未发送'), ('SEND_SUCCESS', '已发送'), ('SEND_FAILURE', '发送失败')], string='过账状态', required=True)
    remark = fields.Char('备注')



