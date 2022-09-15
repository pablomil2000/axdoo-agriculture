# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from datetime import date
from odoo import _, fields, models, api


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
    autonomy_id = fields.Many2one(
        comodel_name='field.notebook.autonomy',
        string='Autonomy',
    )
    autonomy_code = fields.Char(
        related="autonomy_id.code",
        string='Autonomy code',
    )
    province_id = fields.Many2one(
        comodel_name='field.notebook.province',
        string='Province',
    )
    province_code = fields.Char(
        related="province_id.code",
        string='Province code',
    )
    town_id = fields.Many2one(
        comodel_name='field.notebook.town',
        string='Town',
    )
    town_code = fields.Char(
        related="town_id.code",
        string='Town code',
    )
    aggregate = fields.Integer(
        string='Aggregate',
    )
    zone = fields.Integer(
        string='Zone',
    )
    polygon = fields.Integer(
        string='Polygon',
    )
    parcel = fields.Integer(
        string='Parcel',
    )
    surface = fields.Float(
        string='Surface',
        digits=(6, 4),
        default=0.0,
    )
    catastral_reference = fields.Char(
        string="Catastral reference",
    )
    exploitation_id = fields.Many2one(
        comodel_name='field.notebook.exploitation',
        string='Exploitation',
    )
    zone_ids = fields.Many2many(
        string='Zones',
        comodel_name='field.notebook.zone',
        readonly=False,
        store=True,
    )
    system_ids = fields.Many2many(
        string='Systems',
        comodel_name='field.notebook.system',
        readonly=False,
        store=True
    )
    irrigation_id = fields.Many2one(
        string='Irrigation',
        comodel_name='field.notebook.irrigation.system',
        readonly=False,
        store=True
    )
    nursery_ids = fields.One2many(
        comodel_name='field.notebook.parcel.nursery',
        inverse_name='parcel_id',
        string='Nursery',
        copy=True,
        auto_join=True,
    )
    technical_ids = fields.One2many(
        comodel_name='field.notebook.parcel.technical',
        inverse_name='parcel_id',
        string='Technical',
        copy=True,
        auto_join=True,
    )
    enclosure_ids = fields.One2many(
        comodel_name='field.notebook.enclosure',
        inverse_name='parcel_id',
        string='Enclosure',
        readonly=False,
        store=True
    )
    total_plants = fields.Integer(
        string='Total Plants',
    )

    @api.onchange("autonomy_id")
    def _onchange_autonomy_id(self):
        for rec in self:
            return {"domain": {"province_id": [("autonomy_id", "=", rec.autonomy_id.id)]}}

    @api.onchange("province_id")
    def _onchange_province_id(self):
        for rec in self:
            return {"domain": {"town_id": [("province_id", "=", rec.province_id.id)]}}


class FieldNotebookParcelNursery(models.Model):
    _name = 'field.notebook.parcel.nursery'
    _description = 'Parcel Nursery'

    nursery_id = fields.Many2one(
        comodel_name='res.partner',
        string='Nursery',
        required=True,
        domain="[('nursery','=', True)]",
    )
    parcel_id = fields.Many2one(
        comodel_name='field.notebook.parcel',
        string='Parcel',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    plants = fields.Integer(
        string='Plants',
    )
    mortality_percentage = fields.Float(
        string='Mortality percentage',
        digits=(3, 2),
        default=0.0,
    )
    replant = fields.Boolean(
        string='Replant',
        default=False,
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
