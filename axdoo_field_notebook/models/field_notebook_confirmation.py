# Copyright 2023 Antonio Alfaro
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Confirmaciones de actuaciones

from odoo import fields, models


class FieldNotebookConfirmation(models.Model):
    _name = "field.notebook.confirmation"
    _description = "Field Notebook Confirmation"

    name = fields.Char(
        string="Name",
    )
    text_name = fields.Char(
        string="Note",
    )
    ucth_ids = fields.Many2many(
        comodel_name='field.notebook.ucth',
        string='Ucth',
        required=True,
    )
    date_time_start = fields.Datetime(
        string="Date time start",
    )

    date_time_end = fields.Datetime(
        string="Date time end",
    )
    date_time_security = fields.Datetime(
        string="Date time security",
    )
    # date_time_security debe rellenarse de manera automatica segun el plazo de seguridad
    # de los productos utilizados en la Orden de tratamiento
    date_time_harvest = fields.Datetime(
        string="Date time harvest",
    )
    # date_time_harvest se debe importar de la entrada de fruta realizada en Alfinf
    # sugerencia: crear la tabla de recolección y sincronizarla con la de Alfinf
    # con un ODBC PostgreSQL y crear un proceso que rellene el campo date_time_harvest desde esta tabla
    # Objetivo: Controlar los tratamientos fuera de plazado de seguridad
    # Sugerencia 2: Al crear la orden de tratamiento iniciaria la carga de la recoleccion en la tabla confirmation
    # al introducir la fecha hora del tratamiento crearia un proeceso que lo valide
    # y de opcion a dejarlo, eliminarlo o modificarlo
