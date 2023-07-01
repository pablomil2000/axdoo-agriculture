# Copyright 2023 a.Alfinf <antonio@alfinf.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AlfinfControlPanel(models.Model):
    _name = 'alfinf.control.panel'
    _description = "Alfinf Control Panel"

    name = fields.Char(
        string="Name",
        required=True,
    )
    company = fields.Char(
        string="Company",
    )
    family = fields.Char(
        string="family",
    )
    delivery_note = fields.Char(
        string="delivery note",
    )
    invoice = fields.Char(
        string="invoice",
    )
    date_delivery_note = fields.Date(
        string="date delivery note",
    )
    date_invoice = fields.Date(
        string="date delivery note",
    )
    client = fields.Char(
        string="client",
    )
    ucth = fields.Char(
        string="ucth",
    )
    variety_txt = fields.Char(
        string="variety",
    )
    farmer_txt = fields.Char(
        string="farmer",
    )
    external = fields.Boolean(
        string="external",
        default=False
    )
    box = fields.Float(
        string="box",
    )
    format_txt = fields.Char(
        string="format",
    )
    kilos_sale = fields.Float(
        string="kilos sale",
    )
    euro_kilo_sale = fields.Float(
        string="euro kilo sale",
    )
    sale_basis = fields.Float(
        string="sale basis",
    )
    shipper_txt = fields.Char(
        string="shipper",
    )
    truck_registration = fields.Char(
        string="tuck registration",
    )
    farmer_invoice = fields.Char(
        string="farmer invoice",
    )
    date_farmer_invoice = fields.Date(
        string="date farmer invoice",
    )
    date_in_item = fields.Date(
        string="date in item",
    )
    euro_kilo_farmer = fields.Float(
        string="euro kilo farmer",
    )
    buy_basis = fields.Float(
        string="buy basis",
    )
    industry = fields.Boolean(
        string="industry",
    )
    client_county = fields.Char(
        string="client county",
    )
    country_type = fields.Char(
        string="country type",
    )
    not_eec = fields.Boolean(
        string="not ecc",
    )
