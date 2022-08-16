# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from datetime import date
from odoo import _, fields, models


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
    nursery_ids = fields.One2many(
        comodel_name='field.notebook.ucth.nursery',
        inverse_name='ucth_id',
        string='Nursery',
        copy=True,
        auto_join=True,
    )
    technical_ids = fields.One2many(
        comodel_name='field.notebook.ucth.technical',
        inverse_name='ucth_id',
        string='Technical',
        copy=True,
        auto_join=True,
    )
    enclosure_ids = fields.One2many(
        comodel_name='field.notebook.ucth.enclosure',
        inverse_name='ucth_id',
        string='Enclosure',
        copy=True,
        auto_join=True,
    )
    total_plants = fields.Integer(
        string='Total Plants',
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
