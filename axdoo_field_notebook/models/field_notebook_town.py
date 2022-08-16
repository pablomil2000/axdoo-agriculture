# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Campañas

from datetime import date
from odoo import fields, models


class FieldNotebookTown(models.Model):
    _name = "field.notebook.town"
    _description = "Field Notebook Town"

    code_autonomy = fields.Char(
        string="Code Autonomy",
        required=True,
    )
    autonomy_id = fields.Many2one(
        comodel_name='field.notebook.autonomy',
        string="Autonomy",
    )
    code_province = fields.Char(
        string="Code Province",
        required=True,
    )
    province_id = fields.Many2one(
        comodel_name='field.notebook.province',
        string="Province",
    )
    code_town = fields.Char(
        string="Code Town",
        required=True,
    )
    code_control = fields.Char(
        string="Code Control",
        required=True,
    )
    name = fields.Char(
        string="Name",
        required=True,
        index=True,
    )
