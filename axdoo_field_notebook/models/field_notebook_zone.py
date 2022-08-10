# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Zonas

from odoo import fields, models


class FieldNotebookZone(models.Model):
    _name = "field.notebook.zone"
    _description = "Field Notebook Zone"

    name = fields.Char(
        string="Zone Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
