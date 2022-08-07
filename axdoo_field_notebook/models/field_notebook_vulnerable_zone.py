# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FieldNotebookVulnerableZone(models.Model):
    _name = "field.notebook.vulnerable.zone"
    _description = "Field Notebook Vulnerable Zone"

    name = fields.Char(
        string="Vulnerable Zone Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
