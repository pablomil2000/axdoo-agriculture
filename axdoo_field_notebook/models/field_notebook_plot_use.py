# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Uso de parcela

from odoo import fields, models


class FieldNotebookPlotUse(models.Model):
    _name = "field.notebook.plot.use"
    _description = "Field Notebook Plot Use"

    name = fields.Char(
        string="Plot Use Name",
        required=True,
        index=True,
    )
    sequence = fields.Integer(
        default=10,
    )
