# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Plot_Use(models.Model):
    _name = "plot_use"
    _order = "name"
    _description = "plot_use"

    name = fields.Char(required=True)
