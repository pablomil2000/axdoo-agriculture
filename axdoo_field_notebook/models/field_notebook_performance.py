# Copyright 2023 Manuel Calero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Fitosanitarios

from odoo import _, fields, models, api
from odoo.exceptions import ValidationError


class FieldNotebookPerformance(models.Model):
    _name = "field.notebook.performance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Performance"
    _check_company_auto = True

    name = fields.Char(
        string='Name',
        required=True,
        index=True,
        readonly=True,
        default="New",
    )
    # Terapy lo usaremos para tratamientos fitosanitarios que no queremos que aparezcan en el cuaderno de campo
    type = fields.Selection([
        ('phytosanitary', 'Phytosanitary'),
        ('harvest', 'Harvest'),
        ('irrigation', 'Irrigation'),
        ('labor', 'Labor'),
        ('therapy', 'Therapy'),
        ],
        default='phytosanitary',
        required=True,
        tracking=True,
    )
    date = fields.Date(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    date_limit = fields.Date(
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
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        tracking=True,
        required=True,
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
    associate_id = fields.Many2one(
        comodel_name='res.partner',
        string='Associated',
        related="exploitation_id.associate_id",
        required=True,
        tracking=True,
    )
    # ucth_ids = fields.Many2many(
    #     comodel_name='field.notebook.exploitation.ucth',
    #     relation="exploitation_ucth_rel",
    #     required=True,
    #     tracking=True,
    #     domain="[('exploitation_id', '=', exploitation_id)]",
    # )
    agent_ids = fields.Many2many(
        comodel_name='field.notebook.agent',
        tracking=True,
    )
    confirmation_ids = fields.Many2many(
        comodel_name='field.notebook.confirmation',
        string='Confirmation',
    )
    crop_variety_id = fields.Many2one(
        string='Crop Variety',
        comodel_name='field.notebook.crop.variety',
        required=True,
        tracking=True,
    )
    crop_id = fields.Many2one(
        comodel_name='field.notebook.crop',
        string='Crop',
        related="crop_variety_id.crop_id",
        required=True,
        tracking=True,
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
    product_ids = fields.One2many(
        comodel_name='field.notebook.performance.product',
        inverse_name='performance_id',
        string='Products',
        copy=True,
        auto_join=True,
    )
    performance_application_type_id = fields.Many2one(
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
        result = super().create(vals)
        print("Agents_ids",vals.get("agents_ids"))
        print("Type",vals.get("type"))
        if not vals.get("agents_ids") and vals.get("type") == "phytosanitary":
            raise ValidationError(
                _('Agents must be completed.')
            )
        return result

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
        return seq.next_by_code("field.notebook.performance") or "New"

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()


class FieldNotebookPerformanceProducts(models.Model):
    _name = "field.notebook.performance.product"
    _description = "Field Notebook Performance Products"

    sequence = fields.Integer(
        default=10,
    )
    name = fields.Char(
        string='Name',
        index=True,
    )
    performance_id = fields.Many2one(
        comodel_name="field.notebook.performance",
        string="Performance",
        required=True,
        ondelete="cascade",
        index=True,
        copy=False,
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        ondelete='restrict',
        required=True,
        domain="[('phytosanitary', '=', True)]",
    )
    dose = fields.Float(
        string='Dose Kg/ha',
        digits=(16, 2),
        default=0.0,
    )
    application_number = fields.Integer(
        string='Application N.',
    )
    intervals_days = fields.Integer(
        string='Intervals',
    )
    volume_broth = fields.Char(
        string='Vol/Broth',
    )
    specific_conditions = fields.Char(
        string='Conditions',
    )
    crop_id = fields.Many2one(
        comodel_name='field.notebook.crop',
        string='Crop',
        related="performance_id.crop_id",
    )
    agent_ids = fields.Many2many(
        comodel_name='field.notebook.agent',
        string='Agent',
        related="performance_id.agent_ids",
    )

    @api.model
    def name_get(self):
        return [rec.product_id.name for rec in self]

    def _get_product_dose(self):
        product_dose = self.product_id.dose_ids.search(
            [
                ("crop_ids", "=", self.crop_id.id),
                ("agent_ids", "in", self.agent_ids.ids),
            ],
            limit=1,
        )
        return product_dose or None

    @api.onchange('product_id')
    def product_id_change(self):
        self.name = self.product_id.name
        product_dose = self._get_product_dose()
        if product_dose:
            self.dose = product_dose.dose
            self.application_number = product_dose.application_number
            self.intervals_days = product_dose.intervals_days
            self.volume_broth = product_dose.volume_broth
