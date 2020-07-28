from odoo import fields, models, api

class game(models.Model):
    _name = 'test13.game'
    _description = 'Game'

    name = fields.Char ('Game Name')
