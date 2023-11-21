# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    alfinf_id = fields.Float(
        string="Alfinf application id",
    )
    agriculture_format_id = fields.Many2one(
        comodel_name="agriculture.format",
        string="Format",
    )




