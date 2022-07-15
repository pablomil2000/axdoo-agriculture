# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FieldNotebookCrop(models.Model):
    _name = "field.notebook.crop"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Crop"

    name = fields.Char(
        string="Crop Name",
        required=True,
        index=True,
        tracking=True,
    )
