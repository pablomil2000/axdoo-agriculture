# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Zonas

from odoo import fields, models


class FieldNotebookSystem(models.Model):
    _name = "field.notebook.system"
    _description = "Field Notebook System"

    name = fields.Char(
        string="System Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
