# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Crop(models.Model):
    _name = "crop"
    _order = "name"
    _description = "Crop"

    name = fields.Char(required=True)
