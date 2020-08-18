from odoo import fields, models, api

class result(models.Model):
    _name = 'test13_result'
    _description = 'Results'

    name = fields.Char('Name')