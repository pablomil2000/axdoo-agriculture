# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from odoo import _, fields, models, api


class ProductTemplateDose(models.Model):
    _name = 'product.template.dose'
    _description = 'Product Template Dose'

    dose_id = fields.Many2one(
        comodel_name='product.template',
        string='Dose',
    )
    crop_ids = fields.Many2many(
        string='Crop',
        comodel_name='field.notebook.crop',
        required=True,
    )
    agent_ids = fields.Many2many(
        string='Agent',
        comodel_name='field.notebook.agent',
        required=True,
    )
    dose = fields.Float(
        string='Dose Kg/ha',
        digits=(16, 2),
        default=0.0,
        required=True,
    )
    application_number = fields.Integer(
        string='Application N.',
        required=True,
    )
    intervals_days = fields.Integer(
        string='Intervals',
        required=True,
    )
    volume_broth = fields.Char(
        string='Vol/Broth',
    )
    specific_conditions = fields.Char(
        string='Conditions',
    )
