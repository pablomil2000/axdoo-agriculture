# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from odoo import _, fields, models, api


class FieldNotebookProduct(models.Model):
    _name = "field.notebook.product"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Product"

    product_code = fields.Char(
        string="Product Code",
        required=True,
        index=True,
        tracking=True,
    )
    manufacturer_internal_code = fields.Char(
        string="Manufacturer Internal Code",
    )
    registration_number = fields.Char(
        string="Registration Number",
    )
    name = fields.Char(
        string="Name",
        required=True,
        index=True,
        tracking=True,
    )
    # < IdProducto > 36725 < / IdProducto >
    # < CodInternoFabricante / >
    # < NumRegistro >< / NumRegistro >
    # < Nombre >< / Nombre >
    # < Titular ></ Titular >
    # < Fabricante >< / Fabricante >
    # < Fabrica / >
    # < Formulado > < / Formulado >
    # < Estado >< / Estado >
    # < Observaciones / >
    # < Tramite / >
    # < EstadoTramite / >
    # < Condicionamiento >< / Condicionamiento >
    # < Simbolo_1 / >
    # < Simbolo_2 / >
    # < Simbolo_3 / >
    # < Domestico / >
    # < Seg_Almacenamiento >< / Seg_Almacenamiento >
    # < Seg_Manipulacion >< / Seg_Manipulacion >
    # < Seg_Des_Vertido >< / Seg_Des_Vertido >
    # < NRegDirectiva / >
    # < Version / >
    # < VersionDePartida / >
    # < EstadoVersion / >
    # < IdEstado / >
    # < IdSustancia / >
    # < IdAmbito / >
    # < IdCultivo / >
    # < IdPlaga / >
    # < IdFuncion / >
    # < IdTitular / >
    # < IdFormulado >< / IdFormulado >
    # < FechaTramite / >
    # < StrFechaTramite / >
    # < FechaCaducidad >< / FechaCaducidad >
    # < StrFechaCaducidad >< / StrFechaCaducidad >
    # < FechaInscripcion >< / FechaInscripcion >
    # < StrFechaInscripcion >< / StrFechaInscripcion >
    # < FechaRenovacion / >
    # < StrFechaRenovacion / >
    # < FechaModificacion / >
    # < StrFechaModificacion / >
    # < FechaLimiteVenta / >
    # < StrFechaLimiteVenta / >
    # < FechaAutorizacion / >
    # < StrFechaAutorizacion / >

