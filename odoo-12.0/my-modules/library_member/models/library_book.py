from odoo import fields,models

class Book(models.Model):
     _inherit = 'library.book'
     is_available = fields.Boolean('Is Available?')
     isbn = fields.Char(help = "Use a valid ISBN-10 or ISBN-13.")
     publish_id = fields.Many2one(index = True)