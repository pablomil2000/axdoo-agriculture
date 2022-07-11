# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Crop(models.Model):
    _name = "field.notebook.plot.use"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Plot Use"

    name = fields.Char(
        string="Plot Use Name",
        required=True,
        index=True,
        tracking=True,
    )
