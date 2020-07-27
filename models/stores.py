from odoo import fields, models, api

class store(models.Model):
    _name = 'test13.store'
    _description = 'Store'

    name = fields.Char ('Store Name')



