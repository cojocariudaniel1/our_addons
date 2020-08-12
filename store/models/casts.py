from odoo import fields, models, api

class cast(models.Model):
    _name = 'test13.cast'
    _description = 'Casts'

    name = fields.Char('Cast name:')
    age = fields.Integer('Age:')
    gender = fields.Char('Gender:')
    image_cast = fields.Image("Image:", store=True)
    roleplayed = fields.Char('Role played:')

