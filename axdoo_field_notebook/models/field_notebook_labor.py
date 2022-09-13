# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Labores

from odoo import fields, models, api


class FieldNotebookLabor(models.Model):
    _name = "field.notebook.labor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Labor"
    _check_company_auto = True

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.company,
    )
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

    @api.onchange('ucth_id')
    def _onchange_ucth_id(self):
        if self.ucth_id.campaign_id:
            self.campaign_id = self.ucth_id.campaign_id
