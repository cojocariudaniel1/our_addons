from odoo import fields, models, api

class market(models.Model):
    _name = 'test13.market'
    _description = 'Markets'

    name= fields.Char('Name:')
