# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import date
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    technical = fields.Boolean(
        string="Technical",
        help="Check this field if technical is implement.",
    )
    nursery = fields.Boolean(
        string="Nursery",
        help="Check this field if nursery is implement.",
    )
    plant_passport = fields.Char(
        string="Plant Passport",
        help="Fill this field if nursery is implement.",
    )
