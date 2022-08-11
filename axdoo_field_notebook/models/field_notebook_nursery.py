# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Vivero

from odoo import fields, models


class FieldNotebookSystem(models.Model):
    _name = "field.notebook.nursery"
    _description = "Field Notebook System"

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
