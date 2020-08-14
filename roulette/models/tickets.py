from odoo import fields, models, api
class ticket(models.Model):
    _name = 'test13_ticket'
    _description = 'Tickets'


    name = fields.Char('Name')
    ticket_id = fields.Char('Ticket ID.', default='Ticket ID')
    client_ids =
    # on create method
    @api.model
    def create(self, vals):
        obj = super(ticket, self).create(vals)
        if obj.ticket_id == 'Ticket ID':
            number = self.env['ir.sequence'].get('your.sequence.code') or 'Ticket ID'
            obj.write({'ticket_id': number})
        return obj




