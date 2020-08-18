from odoo import fields, models, api

class tickets(models.Model):
    _name = 'test13_ticket'
    _description = 'Tickets'

    number_1 = fields.Integer(required=True, default='')
    number_2 = fields.Integer(required=True, default='')
    number_3 = fields.Integer(required=True, default='')
    number_4 = fields.Integer(required=True, default='')
    number_5 = fields.Integer(required=True, default='')
    number_6 = fields.Integer(required=True, default='')
    active = fields.Boolean(default=True)
    text = fields.Char(default='Buy a ticket:')
    name = fields.Char('Ticket ID', store=True, default='New code')
    price = fields.Integer()


    @api.model
    def create(self, vals):
        if vals.get('name', 'New code') == 'New code':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New code'
        result = super(tickets, self).create(vals)
        return result


