# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Provincias

from datetime import date
from odoo import fields, models


class FieldNotebookProvince(models.Model):
    _name = "field.notebook.province"
    _description = "Field Notebook Province"

    code = fields.Char(
        string="Code",
        required=True,
    )
    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )
