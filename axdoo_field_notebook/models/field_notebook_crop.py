# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Cultivos

from odoo import fields, models


class FieldNotebookCrop(models.Model):
    _name = "field.notebook.crop"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Crop"

    name = fields.Char(
        string="Crop Name",
        required=True,
        index=True,
        tracking=True,
    )
    variety_ids = fields.One2many(
        comodel_name='field.notebook.crop.variety',
        inverse_name='crop_id',
        string='Crop Variety',
    )

class FieldNotebookCropVariety(models.Model):
    _name = 'field.notebook.crop.variety'
    _description = 'Crop Variety'

    variety_id = fields.Many2one(
        comodel_name='field.notebook.variety',
        string='Variety',
        required=True,
        ondelete='cascade',
    )
    crop_id = fields.Many2one(
        comodel_name='field.notebook.crop',
        string='Crop',
        required=True,
        ondelete='cascade',
        index=True,
    )
