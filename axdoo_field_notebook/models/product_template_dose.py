# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from datetime import date
from odoo import _, fields, models, api

class ProductTemplateDose(models.Model):
    _name = 'product.template.dose'
    _description = 'Product Template Dose'

    dose_id = fields.Many2one(
        comodel_name='product.template',
        string='Dose',
    )
    crop_id = fields.Many2one(
        string='Crop',
        comodel_name='field.notebook.crop',
        required=True,
    )
    dose = fields.Float(
        string='Dose',
        digits=(16, 2),
        default=0.0,
        required=True,
    )
