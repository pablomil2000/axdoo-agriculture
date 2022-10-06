# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Labores

import json

from odoo import fields, models, api


class FieldNotebookLabor(models.Model):
    _name = "field.notebook.labor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Labor"
    _check_company_auto = True

    name = fields.Char(
        string='Labor Reference',
        required=True,
        index=True,
        copy=False,
        default="New",
    )
    date_expected = fields.Date(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    date_start = fields.Date(
        index=True,
        tracking=True,
        default=lambda self: fields.Datetime.today(),
    )
    date_end = fields.Date(
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
    ucth_id = fields.Many2one(
        comodel_name='field.notebook.ucth',
        required=True,
        tracking=True,
    )
    exploitation_id = fields.Many2one(
        comodel_name='field.notebook.exploitation',
        related="ucth_id.exploitation_id",
        store=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        related="ucth_id.company_id",
        tracking=True,
        required=True,
    )
    associate_id = fields.Many2one(
        comodel_name='res.partner',
        string='Associated',
        related="ucth_id.associate_id",
        required=True,
        tracking=True,
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        required=True,
        tracking=True,
        domain="[('phytosanitary','=',True),'|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )
    state = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('closed', 'Closed')
    ],
        default='open',
        tracking=True,
    )
    labor_type_id = fields.Many2one(
        comodel_name='field.notebook.labor.type',
    )
    duration = fields.Float(
        group_operator='sum',
    )
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        string='Employees',
    )
    equipment_ids = fields.Many2many(
        comodel_name='maintenance.equipment',
        string='Equipments',
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
        return seq.next_by_code("field.notebook.labor") or "New"

    @api.model
    def _get_campaign_id(self):
        default_campaign_id = self.env["ir.config_parameter"].sudo().get_param("field_notebook.campaign_id")
        if not default_campaign_id:
            return None
        return self.env['field.notebook.campaign'].sudo().browse(int(default_campaign_id)).exists()

    @api.depends('company_id')
    def _compute_associate_id_domain(self):
        for rec in self:
            rec.associate_id_domain = json.dumps(
                [('associate', '=', True), '|', ('company_id', '=', False), ('company_id', '=', rec.company_id.id)]
            )

