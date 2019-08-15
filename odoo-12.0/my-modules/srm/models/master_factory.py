from odoo import models, fields

class factory(models.Model):
    _name = 'srm.master.factory'
    _description = 'factory'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    company_id = fields.Many2one('srm.master.company', string='公司名称')
    remark = fields.Char('备注')




