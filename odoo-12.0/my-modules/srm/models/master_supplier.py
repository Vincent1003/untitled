from odoo import models, fields

class supplier(models.Model):
    _name = 'srm.master.supplier'
    _description = 'supplier'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    abbreviation = fields.Char('简称')
    link_man = fields.Many2one('res.users', string='联系人')
    phone = fields.Char('电话')
    address = fields.Char('地址')
    tax_code = fields.Char('税号', required=True)
    deposit_bank = fields.Char('开户行')
    account = fields.Char('账户')
    email = fields.Char('邮箱')
    fax = fields.Char('传真')
    remark = fields.Char('备注')




