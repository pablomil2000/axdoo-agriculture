# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import date
from odoo import fields, models


class FieldNotebookTechnical(models.Model):
    _name = "field.notebook.technical"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Technical"

    name = fields.Char(
        string="Technical Name",
        required=True,
        index=True,
        tracking=True,
    )
    parcel_ids = fields.Many2one(
        comodel_name='field.notebook.parcel.technical',
        inverse_name='technical_id',
        string='Parcel',
        copy=True,
        auto_join=True,
    )
