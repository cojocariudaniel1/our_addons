from odoo import fields, models, api

class character(models.Model):
    _name = 'test13.character'
    _description = 'Characters'

    name = fields.Char('Character name')
    age = fields.Integer('Age')
    gender = fields.Char('Gender')
    image_128 = fields.Image("Image", store=True)
    id = fields.Char('ID')
    description = fields.Char('Description')
    roleingame = fields.Char('Role in gane')