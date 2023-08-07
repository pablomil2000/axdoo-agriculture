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
    campaign_id = fields.Many2one(
        comodel_name='field.notebook.campaign',
        string='Campaign',
        required=True,
        default=lambda self: self._get_campaign_id(),
    )
    alias = fields.Char(
        string="Alias",
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
    enclosure_ids = fields.One2many(
        string='Enclosures',
        comodel_name='field.notebook.ucth.enclosure',
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
    crop_variety_ids = fields.One2many(
        string='Crop Varieties',
        comodel_name='field.notebook.ucth.crop.variety',
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

    _sql_constraints = [
        (
            "ucth_name_uniq",
            "unique(name, campaign_id, company_id)",
            _("This UCTH name and campaign already exists !"),
        )
    ]

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

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()


class FieldNotebookEnclosure(models.Model):
    _name = 'field.notebook.ucth.enclosure'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Field Notebook UCTH Enclosure'

    name = fields.Char(
        string='Name',
        index=True,
        tracking=True,
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        string='UCTH',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
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
        string='Campaign',
        required=True,
        default=lambda self: self._get_campaign_id(),
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

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()


class FieldNotebookUCTHCropVariety(models.Model):
    _name = 'field.notebook.ucth.crop.variety'
    _description = 'UCTH CropVariety'

    variety_id = fields.Many2one(
        comodel_name='field.notebook.crop.variety',
        string='Crop Variety',
        required=True,
    )
    crop_id = fields.Many2one(
        related="variety_id.crop_id",
        comodel_name="field.notebook.crop",
        string="Crop",
        readonly=True,
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
        string='Campaign',
        required=True,
        default=lambda self: self._get_campaign_id(),
    )

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()

# Deprecated models
#
# class FieldNotebookUCTHEnclosure(models.Model):
#     _name = 'field.notebook.ucth.enclosure'
#     _description = 'UCTH Enclosure'
#
#     enclosure_id = fields.Many2one(
#         comodel_name='field.notebook.enclosure',
#         string='Enclosure',
#         required=True,
#         ondelete='cascade',
#         delegate=True,
#     )
#     ucth_id = fields.Many2one(
#         comodel_name='field.notebook.ucth',
#         string='UCTH',
#         required=True,
#         ondelete='cascade',
#         index=True,
#         copy=False,
#     )
#     campaign_id = fields.Many2one(
#         comodel_name='field.notebook.campaign',
#         string='Campaign',
#         required=True,
#         default=lambda self: self._get_campaign_id(),
#     )
#     surface = fields.Float(
#         string='Surface',
#         digits=(6, 4),
#         default=0.0,
#     )
#
#     @api.model
#     def _get_campaign_id(self):
#         default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
#         if not default_campaign_id:
#             return None
#         return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()
#
#     _sql_constraints = [
#         (
#             "enclosure_uniq",
#             "unique(enclosure_id, ucth_id)",
#             _("This enclosure already exists in this ucth !"),
#         )
#     ]
