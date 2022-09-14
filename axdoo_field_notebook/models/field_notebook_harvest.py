# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Cosecha

from odoo import fields, models, api


class FieldNotebookHarvest(models.Model):
    _name = "field.notebook.harvest"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Harvest"
    _check_company_auto = True

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.company,
    )
    name = fields.Char(
        string='Harvest Reference',
        required=True,
        index=True,
        copy=False,
        default="New",
    )
    date = fields.Date(
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
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        check_company=True,
    )
    commercialization = fields.Selection([
        ('commercialized', 'Commercialized'),
        ('direct', 'Direct')
    ],
        default='commercialized',
        tracking=True,
    )
    lot = fields.Char(
    )
    quantity_kg = fields.Float(
        digits=(16, 2),
        group_operator='sum',
    )
    price = fields.Float(
        digits=(16, 2),
    )
    total_price = fields.Float(
        digits=(16, 2),
        group_operator='sum',
        compute='_compute_total_price',
        store=True,
        readonly=True,
    )

    @api.depends('quantity_kg', 'price')
    def _compute_total_price(self):
        for harvest in self:
            harvest.total_price = harvest.quantity_kg * harvest.price

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
        return seq.next_by_code("field.notebook.harvest") or "New"

    @api.onchange('ucth_id')
    def _onchange_ucth_id(self):
        if self.ucth_id.campaign_id:
            self.campaign_id = self.ucth_id.campaign_id
