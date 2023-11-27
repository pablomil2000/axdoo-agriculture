# Copyright 2023 Alberto alberto@alfinf.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AgricultureBrand(models.Model):
    _name = 'agriculture.brand'

    name = fields.Char(
        string='Name',
        required=True,
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        default=lambda self: self.env.company,
    )
    alfinf_id = fields.Integer(
        string="Alfinf application id",
    )

