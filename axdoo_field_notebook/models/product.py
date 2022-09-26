# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import date
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    phytosanitary = fields.Boolean(
        string="Phytosanitary",
        help="Check this field if phytosanitary product.",
    )
    manufacturer_internal_code = fields.Char(
        string="Manufacturer Internal Code",
    )
    registration_number = fields.Char(
        string="Registration Number",
    )
    product_code = fields.Char(
        string="Product Code",
        index=True,
        tracking=True,
    )
    holder = fields.Char(
        string="Holder",
    )
    manufacturer = fields.Char(
        string="Manufacturer",
    )
    factory = fields.Char(
        string="Factory",
    )
    formulated = fields.Char(
        string="Formulated",
    )
    state = fields.Char(
        string="State",
    )
    observations = fields.Char(
        string="Observations",
    )
    procedure = fields.Char(
        string="Procedure",
    )
    procedure_state = fields.Char(
        string="Procedure state",
    )
    conditioning = fields.Char(
        string="Conditioning",
    )
    symbol_1 = fields.Char(
        string="Symbol 1",
    )
    symbol_2 = fields.Char(
        string="Symbol 2",
    )
    symbol_3 = fields.Char(
        string="Symbol 3",
    )
    domestic = fields.Char(
        string="Domestic",
    )
    storage_security = fields.Char(
        string="Storage security",
    )
    handling_security = fields.Char(
        string="Handling security",
    )
    spill_security = fields.Char(
        string="Spill security",
    )
    directive_registration_number = fields.Char(
        string="Directive registration Number",
    )
    version = fields.Char(
        string="Version",
    )
    departure_version = fields.Char(
        string="Departure version",
    )
    state_version = fields.Char(
        string="State version",
    )
    state_id = fields.Char(
        string="State id",
    )
    substance_id = fields.Char(
        string="Substance id",
    )
    ambit_id = fields.Char(
        string="Ambit id",
    )
    crop_id = fields.Char(
        string="Crop id",
    )
    plague_id = fields.Char(
        string="Plague id",
    )
    function_id = fields.Char(
        string="Function id",
    )
    headline_id = fields.Char(
        string="Headline id",
    )
    formulated_id = fields.Char(
        string="Formulated id",
    )
    procedure_date = fields.Date(
        string="Procedure date",
    )
    expiration_date = fields.Date(
        string="Expiration date",
    )
    inscription_date = fields.Date(
        string="Inscription date",
    )
    renewal_date = fields.Date(
        string="Renewal date",
    )
    modification_date = fields.Date(
        string="Modification date",
    )
    sale_deadline = fields.Date(
        string="Sale deadline date",
    )
    authorization_date = fields.Date(
        string="Authorization date",
    )
    security_term_ids = fields.One2many(
        string='Security Term',
        comodel_name='product.template.security.term',
        inverse_name='security_term_id',
        copy=True,
        auto_join=True,
    )
