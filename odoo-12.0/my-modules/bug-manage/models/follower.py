# -*- coding: utf-8 -*-

from odoo import  models, fields, api

class follower(models.Model):
    _inherit='res.partner'
    bug_ids=fields.Many2many('bm.bug', string='bug')  # 与follower_id字段对应 可以供ORM识别创建后台表
    #  继承了res.partner 增加了bug_ids字段