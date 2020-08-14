from odoo import fields, models, api
class ticket(models.Model):
    _name = 'test13_ticket'
    _description = 'Tickets'

    ticket_id = fields.Char(string='Ticket ID')





