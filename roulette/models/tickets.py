from odoo import fields, models, api

import random

class tickets(models.Model):
    _name = 'test13_ticket'
    _description = 'Tickets'

    active = fields.Boolean(default=True)
    text = fields.Char(default='Buy a ticket:')
    name = fields.Char('Ticket ID', store=True, default='New code')
    price = fields.Integer()

    date = fields.Date(string='Date', default=lambda self: fields.Date.today())

    @api.model
    def create(self, vals):
        if vals.get('name', 'New code') == 'New code':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New code'
        result = super(tickets, self).create(vals)
        return result


    number_1 = fields.Integer(required=True, default='')
    number_2 = fields.Integer(required=True, default='')
    number_3 = fields.Integer(required=True, default='')
    number_4 = fields.Integer(required=True, default='')
    number_5 = fields.Integer(required=True, default='')
    number_6 = fields.Integer(required=True, default='')

    result = fields.Integer(string='Result', compute='_result')

    def _result(self):
        for tickets in self:
            random_list = []
            for i in range(0, 49):
                n = random.randint(0, 49)
                random_list.append(n)

            number_list = []
            number_list.append(tickets.number_1)
            number_list.append(tickets.number_2)
            number_list.append(tickets.number_3)
            number_list.append(tickets.number_4)
            number_list.append(tickets.number_5)
            number_list.append(tickets.number_6)

            number_intersection = list(set(random_list) & set(number_list))
            number_intersection_len = len(number_intersection)

            if number_intersection_len < 1:
                result = 0
            else:
                result = tickets.price * (number_intersection_len * 100)

            tickets.result = result









