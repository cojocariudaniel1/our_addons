from odoo import api, fields, models


class movie(models.Model):
    _name = "test13.movie"
    _description = "Movies"

    name = fields.Char("Movie Name:", required=True)
    launch_date = fields.Date("Launch Date:")
    description_movie = fields.Text("Description:")
    poster = fields.Image("Poster of the Movie:")
    deposit = fields.Integer("Copies of Movie In Deposit")
    price = fields.Monetary("Price:", group_operator="avg")
    rate = fields.Float("Rate:")
    category = fields.Char("Category:")
    currency_id = fields.Many2one(
        "res.currency", "Currency", required=True, default=lambda self: self.env.company.currency_id.id
    )
    actor_ids = fields.Many2many("test13.cast", string="Actors:")

    def button_action1(self):
        self.deposit = self.deposit - 1
