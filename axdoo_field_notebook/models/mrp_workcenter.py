# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class MrpWorkcenter(models.Model):
    _inherit = "mrp.workcenter"

    implement = fields.Boolean(
        string="Implement",
        help="Check this field if the workcenter is implement.",
    )
