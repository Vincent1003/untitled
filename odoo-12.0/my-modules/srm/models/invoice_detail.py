from odoo import models, fields

class invoiceDetail(models.Model):
    _name = 'srm.invoice.detail'
    _description = 'invoice detail'
    invoice_id = fields.Many2one('srm.invoice', string='送货单号', required=True)
    line_code = fields.Char('行号', required=True)
    material_id = fields.Many2one('srm.master.material', string='物料名称', required=True)
    send_quantity = fields.Integer('发货数量', required=True)
    receive_quantity = fields.Integer('收货数量')
    order_id = fields.Many2one('srm.order', string='订单编号', required=True)

