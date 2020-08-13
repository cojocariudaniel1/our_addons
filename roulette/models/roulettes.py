from odoo import fields, models, api
class roulette(models.Model):
    _name = 'test13.roulette'
    _description = 'roulette'

    name = fields.Char ("Roulette Name:")
    id = fields.Char ('ID')
    image = fields.Binary(string="Picture", required=True, store=True)
    image_name = fields.Char("Picture name")
    data = fields.Date('Date')




