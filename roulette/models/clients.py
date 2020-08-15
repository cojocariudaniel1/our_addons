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

    tickets_ids = fields.Many2many('test13_ticket', string = 'Tickets:')

    def method_name(self):
        view_id = self.env.ref('roulette.view_tickets_form').id
        context = self._context.copy()
        return {
            'name':'TicketsForm',
            'view_type':'form',
            'view_mode':'tree',
            'views' : [(view_id,'form')],
            'res_model':'test13_ticket',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'res_id':self.id,
            'target':'new',
            'context':context,
        }


