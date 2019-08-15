from odoo import models, fields

class warehouse(models.Model):
    _name = 'srm.master.warehouse'
    _description = 'warehouse'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    address = fields.Char('地址', required=True)
    factory_id = fields.Many2one('srm.master.factory', string='工厂名称')
    remark = fields.Char('备注')




