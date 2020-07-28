from odoo import fields, models, api

class game(models.Model):
    _name = 'test13.game'
    _description = 'Game'

    name = fields.Char ('Game Name')
    launch_date = fields.Date ('Launch Date')
    description_movie= fields.Text('Description:')
    poster= fields.Image('Poster of the Game:')
    deposit= fields.Integer('Copies of Games licenses in Deposit')
    price= fields.Monetary('Price:')
    rate= fields.Integer('Rate:')
    currency_id= fields.Many2many('test13.store', string= 'Price')
    id = fields.Char('ID')
    character_ids = fields.Many2many('test13.character', string = 'Characters')
