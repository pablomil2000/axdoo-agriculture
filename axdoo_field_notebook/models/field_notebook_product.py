# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Parcela

from odoo import _, fields, models, api


class FieldNotebookProduct(models.Model):
    _name = "field.notebook.product"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Field Notebook Product"

    name = fields.Char(
        string="Name",
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

    # < IdProducto > 36725 < / IdProducto >***product_code***
    # < CodInternoFabricante / >***manufacturer_internal_code***
    # < NumRegistro >< / NumRegistro >***registration_number***
    # < Nombre >< / Nombre >***name***
    # < Titular ></ Titular >***holder***
    # < Fabricante >< / Fabricante >***manufacturer***
    # < Fabrica / >***factory***
    # < Formulado > < / Formulado >***formulated***
    # < Estado >< / Estado >***state***
    # < Observaciones / >***observations***
    # < Tramite / >***procedure***
    # < EstadoTramite / >***procedure_state***
    # < Condicionamiento >< / Condicionamiento >***consitioning***
    # < Simbolo_1 / >***symbol_1***
    # < Simbolo_2 / >***symbol_2***
    # < Simbolo_3 / >***symbol_3***
    # < Domestico / >***domestic***
    # < Seg_Almacenamiento >< / Seg_Almacenamiento >***storage_security***
    # < Seg_Manipulacion >< / Seg_Manipulacion >***handling_security***
    # < Seg_Des_Vertido >< / Seg_Des_Vertido >***spill_security***
    # < NRegDirectiva / >***directive_registration_number***
    # < Version / >***version***
    # < VersionDePartida / >***departure_version***
    # < EstadoVersion / >***state_version***
    # < IdEstado / >***state_id***
    # < IdSustancia / >***substance_id***
    # < IdAmbito / >***ambit_id***
    # < IdCultivo / >***crop_id***
    # < IdPlaga / >***plague_id***
    # < IdFuncion / >***function_id***
    # < IdTitular / >***headline_id***
    # < IdFormulado >< / IdFormulado >***formulated_id***
    # < FechaTramite / >***procedure_date***
    # < StrFechaTramite / >***comment_procedure_date***
    # < FechaCaducidad >< / FechaCaducidad >***expiration_date***
    # < StrFechaCaducidad >< / StrFechaCaducidad >***comment_expiration_date***
    # < FechaInscripcion >< / FechaInscripcion >***inscription_date***
    # < StrFechaInscripcion >< / StrFechaInscripcion >***comment_inscription_date***
    # < FechaRenovacion / >***renewal_date***
    # < StrFechaRenovacion / >***comment_renewal_date***
    # < FechaModificacion / >***modification_date***
    # < StrFechaModificacion / >***comment_modification_date***
    # < FechaLimiteVenta / >***sale_deadline***
    # < StrFechaLimiteVenta / >***comment_sale_deadline***
    # < FechaAutorizacion / >***authorization_date***
    # < StrFechaAutorizacion / >***comment_authorization_date***

