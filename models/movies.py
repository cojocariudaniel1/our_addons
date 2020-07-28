from odoo import fields, models, api

class movie(models.Model):
    _name = 'test13.movie'
    _description = 'Movies'

    name = fields.Char ('Movie Name')
