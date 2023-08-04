# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Campañas

from datetime import date
from odoo import fields, models


class FieldNotebookCampaign(models.Model):
    _name = "field.notebook.campaign"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Campaign"

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
        tracking=True,
    )
    is_year = fields.Boolean(
        string="Year",
        help="Check this field if campaign is annual.",
    )
    year = fields.Integer(
        string="Year of harvest",
        default=date.today().year,
    )
    start_date = fields.Date(
        string="Start Date",
    )
    end_date = fields.Date(
        string="End Date",
    )
    sampling_units = fields.Integer(
        string="Sampling Units",
    )

