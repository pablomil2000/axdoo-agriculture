# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Recintos

from odoo import fields, models


class FieldNotebookEnclosure(models.Model):
    _name = "field.notebook.enclosure"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Enclosure"

    parcel_id = fields.Many2one(
        comodel_name='field.notebook.parcel',
        string='Parcel',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    name = fields.Char(
        string='Enclosure Name',
        index=True,
        tracking=True,
    )
    enclosure = fields.Float(
        string='Enclosure Number',
        digits=(6, 0),
        default=0.0,
        index=True,
        tracking=True,
    )
    plot_use_id = fields.Many2one(
        comodel_name='field.notebook.plot.use',
        string='Plot Use',
        copy=True,
        auto_join=True,
    )
    surface = fields.Float(
        string='Surface',
        digits=(6, 4),
        default=0.0,
    )
    slope = fields.Float(
        string='Slope',
        digits=(6, 2),
        default=0.0,
    )
    irrigation_coefficient = fields.Float(
        string='Irrigation Coefficient',
        digits=(6, 2),
        default=0.0,
    )
    region = fields.Float(
        string='Region',
        digits=(6, 0),
        default=0.0,
    )
