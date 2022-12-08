# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    alfinf_id = fields.Float(
        string="Alfinf application id",
    )

    def create_invoices(self, grouped=False, final=False, date=None):
        return self._create_invoices(grouped, final, date)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    alfinf_id = fields.Float(
        string="Alfinf application id",
    )
    
