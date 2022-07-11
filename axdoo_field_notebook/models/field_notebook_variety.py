# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Crop(models.Model):
    _name = "field.notebook.variety"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Variety"

    name = fields.Char(
        string="Variety Name",
        required=True,
        index=True,
        tracking=True,
    )
