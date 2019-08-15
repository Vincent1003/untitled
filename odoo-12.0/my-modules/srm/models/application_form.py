from odoo import models, fields

class applicationForm(models.Model):
    _name= 'srm.application.form'
    _description = 'srm applicaion_form'
    no= fields.Char('编号',required=True)
    formName = fields.Char('申请单名称',required=True)
    state = fields.Selection([('DONE', '审批完成'), ('PROCESSING', '审批中')],string='状态',required=True)
    type = fields.Selection([('INVOICE_CANCEL','送货单取消'),
                            ('INVOICE_REFUND','送货单退货'),
                            ('ORDER_MODIFY','订单修改'),
                            ('STATEMENT_SUBMIT','结算单提交审批')],
                           string='类型',
                           required=True)
    applicant = fields.Char('申请人',required=True)





