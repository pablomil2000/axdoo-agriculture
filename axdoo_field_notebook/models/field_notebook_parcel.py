# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class FieldNotebookParcel(models.Model):
    _name = "field.notebook.parcel"
    _description = "Field Notebook Parcel"

    name = fields.Char("Parcel Name", required=True, index=True)


