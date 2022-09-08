# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Fitosanitarios

from odoo import fields, models, api


class FieldNotebookPhytosanitary(models.Model):
    _name = "field.notebook.phytosanitary"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Phytosanitary"

    name = fields.Char(
        string='Phytosanitary Reference',
        required=True,
        index=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('field.notebook.phytosanitary'),
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
    )
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        required=True,
        tracking=True,
    )
    exploitation_id = fields.Many2one(
        comodel_name='field.notebook.exploitation',
        related="ucth_id.exploitation_id",
        store=True,
    )
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Employees',
    )
    equipment_ids = fields.Many2many(
        comodel_name='maintenance.equipment',
        string='Equipments',
    )
    product_id = fields.Many2one(
        comodel_name='field.notebook.product',
        required=True,
        tracking=True,
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

    @api.onchange('ucth_id')
    def _onchange_ucth_id(self):
        if self.ucth_id.campaign_id:
            self.campaign_id = self.ucth_id.campaign_id
