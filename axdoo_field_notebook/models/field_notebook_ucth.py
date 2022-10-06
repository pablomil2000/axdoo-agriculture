# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# UCTH

import json

from odoo import _, fields, models, api


class FieldNotebookUCTH(models.Model):
    _name = "field.notebook.ucth"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook UCTH"

    name = fields.Char(
        string="UCTH Name",
        required=True,
        index=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    associate_id = fields.Many2one(
        comodel_name='res.partner',
        string='Associated',
        required=True,
    )
    associate_id_domain = fields.Char(
        compute="_compute_associate_id_domain",
        readonly=True,
        store=False,
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
        comodel_name='field.notebook.irrigation.system',
        readonly=False,
        store=True
    )
    parcel_ids = fields.One2many(
        string='Parcels',
        comodel_name='field.notebook.ucth.parcel',
        inverse_name='ucth_id',
        copy=True,
        auto_join=True,
    )
    nursery_ids = fields.One2many(
        string='Nursery',
        comodel_name='field.notebook.ucth.nursery',
        inverse_name='ucth_id',
        copy=True,
        auto_join=True,
    )
    technical_ids = fields.One2many(
        string='Technical',
        comodel_name='field.notebook.ucth.technical',
        inverse_name='ucth_id',
        copy=True,
        auto_join=True,
    )
    enclosure_ids = fields.One2many(
        string='Enclosure',
        comodel_name='field.notebook.ucth.enclosure',
        inverse_name='ucth_id',
        copy=True,
        auto_join=True,
    )
    total_plants = fields.Integer(
        string='Total Plants',
    )
    crop_id = fields.Many2one(
        string='Crop',
        comodel_name='field.notebook.crop',
        readonly=False,
        store=True
    )
    crop_variety_id = fields.Many2one(
        string='Crop Variety',
        comodel_name='field.notebook.crop.variety',
        readonly=False,
        store=True
    )

    @api.onchange("autonomy_id")
    def _onchange_crop_id(self):
        for rec in self:
            return {"domain": {"crop_variety_id": [("crop_id", "=", rec.crop_id.id)]}}

    @api.depends('company_id')
    def _compute_associate_id_domain(self):
        for rec in self:
            rec.associate_id_domain = json.dumps(
                [('associate', '=', True), '|', ('company_id', '=', False), ('company_id', '=', rec.company_id.id)]
            )


class FieldNotebookUCTHParcel(models.Model):
    _name = 'field.notebook.ucth.parcel'
    _description = 'UCTH Parcel'

    parcel_id = fields.Many2one(
        string='Parcels',
        comodel_name='field.notebook.parcel',
        required=True,
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        string='UCTH',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    surface = fields.Float(
        string='Surface',
        digits=(6, 4),
        default=0.0,
    )


class FieldNotebookUCTHNursery(models.Model):
    _name = 'field.notebook.ucth.nursery'
    _description = 'UCTH Nursery'

    nursery_id = fields.Many2one(
        comodel_name='res.partner',
        string='Nursery',
        required=True,
        domain="[('nursery','=', True)]",
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        string='UCTH',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    campaign_id = fields.Many2one(
        comodel_name='field.notebook.campaign',
        tracking=True,
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


class FieldNotebookUCTHTechnical(models.Model):
    _name = 'field.notebook.ucth.technical'
    _description = 'UCTH Technical'

    technical_id = fields.Many2one(
        comodel_name='res.partner',
        string='Technical',
        required=True,
        domain="[('technical','=', True)]",
        check_company=True,
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        string='UCTH',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )

    _sql_constraints = [
        (
            "technical_uniq",
            "unique(technical_id, ucth_id)",
            _("This technical already exists in this ucth !"),
        )
    ]


class FieldNotebookUCTHEnclosure(models.Model):
    _name = 'field.notebook.ucth.enclosure'
    _description = 'UCTH Enclosure'

    enclosure_id = fields.Many2one(
        comodel_name='field.notebook.enclosure',
        string='Enclosure',
        required=True,
        ondelete='cascade',
        delegate=True,
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        string='UCTH',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    _sql_constraints = [
        (
            "enclosure_uniq",
            "unique(enclosure_id, ucth_id)",
            _("This enclosure already exists in this ucth !"),
        )
    ]
