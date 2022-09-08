# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Tipos de Aplicaciones de Tratamientos Fitosanitarios

from odoo import fields, models


class FieldNotebookPhytosanitaryApplicationType(models.Model):
    _name = "field.notebook.phytosanitary.application.type"
    _description = "Field Notebook Phytosanitary Application Type"

    name = fields.Char(
        string="Name",
    )
    sequence = fields.Integer(
        default=10,
    )

