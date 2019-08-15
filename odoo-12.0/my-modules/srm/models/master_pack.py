from odoo import models, fields

class pack(models.Model):
    _name = 'srm.master.pack'
    _description = 'pack'
    material_id = fields.Many2one('srm.master.material', string='物料', required=True)
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    capacity = fields.Char('容量', required=True)
    unit = fields.Char('单位', required=True)
    remark = fields.Char('备注')




