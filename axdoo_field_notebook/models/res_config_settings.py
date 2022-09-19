# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    campaign_id = fields.Many2one(
        comodel_name='field.notebook.campaign',
        string='Set default campaign',
        readonly=False,
    )

