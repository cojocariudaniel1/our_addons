from odoo import models, fields, api

class result(models.TransientModel):
    _name = 'result_wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    tickets_id = fields.Many2one('test13_ticket', string='Results' )