# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Zonas

from odoo import fields, models


class FieldNotebookIrrigationSystem(models.Model):
    _name = "field.notebook.irrigation.system"
    _description = "Field Notebook Irrigation System"

    name = fields.Char(
        string="Irrigation Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
