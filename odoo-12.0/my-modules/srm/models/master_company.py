from odoo import models, fields

class company(models.Model):
    _name = 'srm.master.company'
    _description = 'company'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    abbreviation = fields.Char('简称')
    link_man = fields.Char('联系人')
    phone = fields.Char('电话')
    address = fields.Char('地址')
    tax_code = fields.Char('税号', required=True)
    fax = fields.Char('传真')
    remark = fields.Char('备注')




