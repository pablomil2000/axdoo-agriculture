# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Recintos

from datetime import date
from odoo import fields, models


class FieldNotebookEnclosure(models.Model):
    _name = "field.notebook.enclosure"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Enclosure"

    name = fields.Char(
        string="Enclosure Name",
        required=True,
        index=True,
        tracking=True,
    )
    parcel_ids = fields.Many2one(
        comodel_name='field.notebook.parcel.enclosure',
        string='Parcels',
        copy=True,
        auto_join=True,
    )
