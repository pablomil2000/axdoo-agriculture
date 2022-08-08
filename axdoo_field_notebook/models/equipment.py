# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Maquinaria

from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    implement = fields.Boolean(
        string="Implement",
        help="Check this field if the equipment is implement.",
    )
