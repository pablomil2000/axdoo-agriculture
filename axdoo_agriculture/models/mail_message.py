# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields


class MailMessage(models.Model):
    """ Override MailMessage class in order to add a new type: SMS messages.
    Those messages comes with their own notification method, using SMS
    gateway. """
    _inherit = 'mail.message'

    agriculture_type = fields.Selection([
            ('delivery', "Delivery Note"),
            ('wrc', "WRC"),
            ('packing_list', "Packing List"),
            ('bill_lading', "Bill of Lading"),
            ('budget', "Budget"),
            ('sale_order', "Sale Order"),
            ('invoice', "Invoice"),
        ],
        default='delivery',
        copy=False,
        string="Type",
        tracking=True
    )

