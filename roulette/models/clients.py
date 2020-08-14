from odoo import fields, models, api

class client(models.Model):
    _name = 'test13_client'
    _description = 'Clients'

    name = fields.Char('Full name: ')
    age = fields.Integer('Age: ')
    phone = fields.Integer('Phone: ')
    email = fields.Char('Email: ')
    addres = fields.Char('Addres: ')




