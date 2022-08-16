# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Autonomía

from datetime import date
from odoo import fields, models


class FieldNotebookAutonomy(models.Model):
    _name = "field.notebook.autonomy"
    _description = "Field Notebook Autonomy"

    code = fields.Char(
        string="Code",
        required=True,
    )
    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )
