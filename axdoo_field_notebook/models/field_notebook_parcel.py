# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from datetime import date
from odoo import _, fields, models


class FieldNotebookParcel(models.Model):
    _name = "field.notebook.parcel"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Parcel"

    name = fields.Char(
        string="Parcel Name",
        required=True,
        index=True,
        tracking=True,
    )
    campaign_id = fields.Many2one(
        comodel_name='field.notebook.campaign',
        required=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    exploitation_id = fields.Many2one(
        comodel_name='field.notebook.exploitation',
        string='Exploitation',
    )
    zone_ids = fields.Many2many(
        string='Zone',
        comodel_name='field.notebook.zone',
        readonly=False,
        store=True,
    )
    system_ids = fields.Many2many(
        string='System',
        comodel_name='field.notebook.system',
        readonly=False,
        store=True
    )
    irrigation_id = fields.Many2one(
        string='Irrigation',
        comodel_name='field.notebook.irrigation',
        readonly=False,
        store=True
    )
    technical_ids = fields.One2many(
        comodel_name='field.notebook.parcel.technical',
        inverse_name='parcel_id',
        string='Technical',
        copy=True,
        auto_join=True,
    )
    enclosure_ids = fields.One2many(
        comodel_name='field.notebook.parcel.enclosure',
        inverse_name='parcel_id',
        string='Enclosure',
        copy=True,
        auto_join=True,
    )

class FieldNotebookParcelTechnical(models.Model):
    _name = 'field.notebook.parcel.technical'
    _description = 'Parcel Technical'

    technical_id = fields.Many2one(
        comodel_name='res.partner',
        string='Technical',
        required=True,
        domain="[('technical','=', True)]",
        check_company=True,
    )
    parcel_id = fields.Many2one(
        comodel_name='field.notebook.parcel',
        string='Parcel',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )

    _sql_constraints = [
        (
            "technical_uniq",
            "unique(technical_id, parcel_id)",
            _("This technical already exists in this parcel !"),
        )
    ]

class FieldNotebookParcelEnclosure(models.Model):
    _name = 'field.notebook.parcel.enclosure'
    _description = 'Parcel Enclosure'

    enclosure_id = fields.Many2one(
        comodel_name='field.notebook.enclosure',
        string='Enclosure',
        required=True,
        ondelete='cascade',
        delegate=True,
    )
    parcel_id = fields.Many2one(
        comodel_name='field.notebook.parcel',
        string='Parcel',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    _sql_constraints = [
        (
            "enclosure_uniq",
            "unique(enclosure_id, parcel_id)",
            _("This enclosure already exists in this parcel !"),
        )
    ]
