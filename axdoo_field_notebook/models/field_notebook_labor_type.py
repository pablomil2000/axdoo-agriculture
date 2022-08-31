# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Tipos de Labores

from odoo import fields, models


class FieldNotebookLaborType(models.Model):
    _name = "field.notebook.labor.type"
    _description = "Field Notebook Labor Type"

    name = fields.Char(
        string="Name",
    )

