# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Variety(models.Model):
    _name = "variety"
    _order = "name"
    _description = "Variety"

    name = fields.Char(required=True)
