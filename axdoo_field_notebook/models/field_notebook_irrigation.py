# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Zonas

from odoo import fields, models


class FieldNotebookIrrigation(models.Model):
    _name = "field.notebook.irrigation"
    _description = "Field Notebook Irrigation"

    name = fields.Char(
        string="Irrigation Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
