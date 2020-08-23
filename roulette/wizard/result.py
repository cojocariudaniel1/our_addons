from odoo import models, fields, api

class result(models.TransientModel):
    _name = 'result_wizard'
    _description = "Wizard"

    def _default_session(self):
        return self.env['test13_ticket'].browse(self._context.get('Ticket ID'))

    tickets_id = fields.Many2one('test13_ticket', string='Results', default=_default_session)

    attende_ids = fields.Many2one('test13_client', string='Client')

    def test(self):
        for session in self.tickets_id:
            session.attende_ids |= self.attende_ids
        return {}