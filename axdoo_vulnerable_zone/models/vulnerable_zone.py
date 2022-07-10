# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Vulnerable_Zone(models.Model):
    _name = "vulnerable_zone"
    _order = "name"
    _description = "vulnerable_zone"

    name = fields.Char(required=True)
