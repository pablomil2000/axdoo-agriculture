# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AgricultureFormat(models.Model):
    _name = 'agriculture.format'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Agriculture Format"

    name = fields.Char(
        string="Name",
        required=True,
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        tracking=True,
        default=lambda self: self.env.company,
    )
    alfinf_id = fields.Float(
        string="Alfinf application id",
    )
    format = fields.Float(
        string="Units format",
    )
    units = fields.Integer(
        string="Number of units in a box",
    )
    pieces = fields.Integer(
        string="Number of pieces in a tub",
    )
    quality_category = fields.Integer(
        string="Quality category",
    )
    container_field = fields.Float(
        string="Container field",
    )
    container_sale = fields.Float(
        string="Container sale",
    )
    kg_cost = fields.Float(
        string="Cost by kg",
    )
    # Granel
    bulk = fields.Boolean(
        string="Bulk",
    )
    input_output = fields.Selection(
        selection=[
            ("input", "Input"),
            ("output", "Output"),
            ("both", "Input and Output"),
        ],
        string="Format use",
        default="both",
    )
    pda_selection = fields.Boolean(
        string="PDA selection",
    )

