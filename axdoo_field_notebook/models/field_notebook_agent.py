# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Tipos de Aplicaciones de Tratamientos Fitosanitarios

from odoo import fields, models


class FieldNotebookAgent(models.Model):
    _name = "field.notebook.agent"
    _description = "Field Notebook Agent"

    name = fields.Char(
        string="Name",
    )
