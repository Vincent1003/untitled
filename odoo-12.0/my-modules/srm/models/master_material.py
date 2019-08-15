from odoo import models, fields

class material(models.Model):
    _name = 'srm.master.material'
    _description = 'material'
    name = fields.Char('名称', required=True)
    code = fields.Char('代码', required=True)
    standard = fields.Char('规格')
    unit = fields.Char('单位')
    description = fields.Char('描述')
    remark = fields.Char('备注')




