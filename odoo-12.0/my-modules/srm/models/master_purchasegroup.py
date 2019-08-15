from odoo import models, fields

class purchasegroup(models.Model):
    _name = 'srm.master.purchasegroup'
    _description = 'purchasegroup'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    remark = fields.Char('备注')




