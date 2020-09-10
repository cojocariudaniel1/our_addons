from odoo import api, fields, models


class store(models.Model):
    _name = "test13.store"
    _description = "Store"

    name = fields.Char("Store Name:")
    id = fields.Char("ID")
    image = fields.Binary(string="Picture", required=True, store=True)
    games_ids = fields.Many2many("test13.game", string="Games name:")
    movies_ids = fields.Many2many("test13.movie", string="Movie name:")
    image_name = fields.Char("Picture name")
    image_small = fields.Image(
        "Small-sized Image", related="image_original", max_width=64, max_height=64, store=True, help="64px * 64px"
    )
