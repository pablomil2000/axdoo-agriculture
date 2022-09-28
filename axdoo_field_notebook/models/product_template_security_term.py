# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from datetime import date
from odoo import _, fields, models, api

class ProductTemplateSecurityTerm(models.Model):
    _name = 'product.template.security.term'
    _description = 'Product Template Security Term'

    security_term_id = fields.Many2one(
        comodel_name='product.template',
        string='Security Term',
    )
    crop_ids = fields.Many2many(
        string='Crop',
        comodel_name='field.notebook.crop',
        required=True,
    )
    days_of_security = fields.Integer(
        string='Days of security',
        required=True,
    )
