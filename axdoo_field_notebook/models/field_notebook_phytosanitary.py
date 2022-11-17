# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Fitosanitarios

import json

from odoo import fields, models, api


class FieldNotebookPhytosanitary(models.Model):
    _name = "field.notebook.phytosanitary"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Phytosanitary"
    _check_company_auto = True

    name = fields.Char(
        string='Phytosanitary Reference',
        required=True,
        index=True,
        readonly=True,
        default="New",
    )
    date_expected = fields.Date(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    date_start = fields.Datetime(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    date_end = fields.Datetime(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    campaign_id = fields.Many2one(
        comodel_name='field.notebook.campaign',
        required=True,
        tracking=True,
        default=lambda self: self._get_campaign_id(),
    )
    exploitation_id = fields.Many2one(
        comodel_name='field.notebook.exploitation',
        store=True,
        required=True,
    )
    ucth_ids = fields.Many2many(
        comodel_name='field.notebook.exploitation.ucth',
        relation="exploitation_ucth_rel",
        required=True,
        tracking=True,
        domain="[('exploitation_id', '=', exploitation_id)]",
    )
    associate_id = fields.Many2one(
        comodel_name='res.partner',
        string='Associated',
        related="exploitation_id.associate_id",
        required=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        related="associate_id.company_id",
        tracking=True,
        required=True,
    )
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Employees',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    equipment_ids = fields.Many2many(
        comodel_name='maintenance.equipment',
        string='Equipments',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        required=True,
        tracking=True,
        domain="[('phytosanitary','=',True),'|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    phytosanitary_application_type_id = fields.Many2one(
        comodel_name='field.notebook.phytosanitary.application.type',
        tracking=True,
    )
    justify = fields.Selection([
        ('others', '(Others)'),
        ('threshold_crossing', 'Threshold crossing'),
        ('monitoring', 'Monitoring'),
        ('meteorological_conditions', 'Meteorological conditions'),
    ],
        default='others',
        tracking=True,
    )
    emergency = fields.Selection([
        ('none', '(None)'),
        ('pre_emergency', 'Pre emergency'),
        ('post_emergency', 'Post emergency'),
        ('pre_crops', 'Pre crops'),
    ],
        default='none',
        tracking=True,
    )
    wind_speed = fields.Selection([
        ('none', '(None)'),
        ('less', 'Less than 15 km'),
        ('greater', 'Greater than 15km'),
    ],
        default='none',
        tracking=True,
    )
    execution = fields.Selection([
        ('own', 'Own'),
        ('hired', 'Hired'),
    ],
        default='own',
        tracking=True,
    )
    problematic = fields.Selection([
        ('weeds', 'Weeds'),
        ('diseases', 'Diseases'),
        ('pests', 'Pests'),
    ],
        default='weeds',
        tracking=True,
    )
    efficiency = fields.Selection([
        ('good', 'Good'),
        ('bad', 'Bad'),
        ('regular', 'Regular'),
    ],
        default='good',
        tracking=True,
    )
    weather_condition = fields.Selection([
        ('none', '(None)'),
        ('very_cloudy', 'Very cloudy'),
        ('cloudy', 'Cloudy'),
        ('sunny', 'Sunny'),
    ],
        default='none',
        tracking=True,
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self._prepare_name(vals)
        return super().create(vals)

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if "name" not in default:
            default["name"] = self._prepare_name(default)
        return super().copy(default)

    def _prepare_name(self, values):
        seq = self.env["ir.sequence"]
        if "company_id" in values:
            seq = seq.with_company(values["company_id"])
        return seq.next_by_code("field.notebook.phytosanitary") or "New"

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()

    # @api.onchange('ucth_id')
    # def _onchange_ucth_id(self):
    #     if self.ucth_id.campaign_id and self.ucth_id.campaign_id != self.campaign_id:
    #         self.campaign_id = self.ucth_id.campaign_id
