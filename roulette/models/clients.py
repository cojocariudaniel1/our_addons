from odoo import fields, models, api

class client(models.Model):
    _name = 'test13_client'
    _description = 'Clients'

    ceva = fields.Char('Email: ')
    name = fields.Char(string='Name', required=True)
    age = fields.Integer('Age: ')
    phone = fields.Integer('Phone: ')
    email = fields.Char('Email: ')
    addres = fields.Char('Addres: ')
    active = fields.Boolean(default=True)

    tickets_ids = fields.One2many('test13_ticket', 'name')



