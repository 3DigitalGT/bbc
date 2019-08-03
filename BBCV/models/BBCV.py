# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    operator_id = fields.Many2one('res.users', string='Operator', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)
    flete_mbl = fields.Selection([
                    ('C3','Collect'),
                    ('C4','Prepaid')
    ],'Flete mbl p')
    flete_hbl = fields.Selection([
                    ('C1','Collect'),
                    ('C2','Prepaid')
    ],'Flete hbl p')
    so_frecuencia = fields.Many2one('so_frecuencia1','Frecuencia SO')
    o_cotizaciones1 = fields.Char('Ofrecimiento Especial Cotizacion')
    status_socomercial = fields.Many2one('estatus_socomercial','Estatus Comercial')
    no_contenedor = fields.Char('Contenedor')
    o_cotizaciones = fields.Many2one('o_cotizacion','Ofrecimiento Especial Cotizacion')
    total_prepaid = fields.Char('Total Prepaid')
    total_collect = fields.Char('Total Collect')
    date_by = fields.Char('Date By')
    on = fields.Char('On')
    so_by = fields.Char('By')
    observaciones_oper = fields.Text('Observaciones')
    place_delivery = fields.Char('Place of delivery by on carrier')
    discharge = fields.Char('Port of Discharge')
    port = fields.Char('Port of Loading')
    shipper1 = fields.Char('Empresa')
    shipper2 = fields.Char('Contacto')
    shipper3 = fields.Char('Direccion')
    shipper4 = fields.Char('Telefono')
    shipper5 = fields.Char('No de orden')
    shipper6 = fields.Char('Otros')
    shipper7 = fields.Char('Referencia proveedor')
    shipper_landing = fields.Char('Booking No')
    shipper_booking = fields.Char('Bill of lading No')
    shipper_export = fields.Char('Export references')
    consignatario1 = fields.Char('Empresa')
    consignatario2 = fields.Char('contacto')
    consignatario3 = fields.Char('Direccion')
    consignatario4 = fields.Char('Telefono')
    consignatario5 = fields.Char('No de orden')
    consignatario6 = fields.Char('Otros')
    consignatario7 = fields.Char('Agente de carga')
    consignatario8 = fields.Char('Punto y Pais de Origen de Carga')
    consignatario_forwarding = fields.Char('Forwarding')
    consignatario_point = fields.Char('Point and country')
    consignatario_notify = fields.Char('Notify party')
    consignatario_delivery = fields.Char('For delivery')
    primerfa = fields.Selection([
                    ('3','No aplica'),
                    ('1','Si'),
                    ('2','No')
    ],'Primer facturacion a1')
    segundafa = fields.Selection([
                    ('3','No aplica'),
                    ('3','Si'),
                    ('4','No')
    ],'Segunda facturacion a2')
    tercerafa = fields.Selection([
                    ('3','No aplica'),
                    ('5','Si'),
                    ('6','No')
    ],'Tercer facturacion a3')
    cuartafa = fields.Selection([
                    ('3','No aplica'),
                    ('7','Si'),
                    ('8','No')
    ],'cuarta facturacion a4')
    no_fact1 = fields.Char('No de factura a1')
    no_fact2 = fields.Char('No de factura a2')
    no_fact3 = fields.Char('No de factura a3')
    no_fact4 = fields.Char('No de factura a4')
    document = fields.Char('No de documento a1')
    document1 = fields.Char('No de documento a2')
    oc1 = fields.Char('No de OC a1')
    oc2 = fields.Char('No de OC a2')
    oc3 = fields.Char('No de OC a3')
    oc4 = fields.Char('No de OC a4')
    factura9 = fields.Many2one('fac_cliente','Facturacion')
    factura10 = fields.Many2one('fac_prov','Tipo de Factura del Proveedor')
    factura11 = fields.Many2one('fac1','OC 1 Facturacion')
    factura12 = fields.Many2one('fac2','OC 2 Facturacion')
    factura13 = fields.Many2one('fac3','OC 3 Facturacion')
    factura14 = fields.Many2one('fac4','OC 4 Facturacion')
    comision_ventas = fields.Many2one('comision_venta','Comisiones Pagadas de Ventas')
    comision_pagadas = fields.Many2one('comision_pag','Comisiones Pagadas de Operaciones')
    observaciones_facturacion = fields.Text('Observaciones')
    factura1 = fields.Many2one('primer_fac','1er Facturacion')
    factura2 = fields.Many2one('segunda_fac','2da Facturacion')
    factura3 = fields.Many2one('tercer_fac','3ra Facturacion')
    factura4 = fields.Many2one('cuarta_fac','4ta Facturacion')
    factura5 = fields.Many2one('fact1','OC 1er Facturacion')
    factura6 = fields.Many2one('fact2','OC 2da Facturacion')
    factura7 = fields.Many2one('fact3','OC 3ra Facturacion')
    factura8 = fields.Many2one('fact4','OC 4ta Facturacion')
    liquidaciones = fields.Many2one('liquidacion_gasto','Titulo Sin Filtro')
    gastosri = fields.Many2one('gastos_ri','Liquidacion Gastos RI')
    gastos_demoras = fields.Many2one('gasto_demora','Liquidacion Gastos Demoras')
    gastos_almacenajes = fields.Many2one('gasto_almacen','Liquidacion Gastos Almacenaje')
    liquidaciones_estadias = fields.Many2one('liquidacion_estadia','Liquidacion de Gastos Estadias')
    fecha_devolucion = fields.Date('Fecha Devolucion del Contenedor')
    devoluciones_garantias = fields.Many2one('devolucion_garantia','Devolucion de Depositos en Garantia')
    fecha_finalizacion = fields.Date('Fecha Finalizacion de la Operacion')
    valor_estadias = fields.Char('valor Estadias de Transportes')
    bbc_almacenaje = fields.Integer('Dias Almacenaje')
    bbc_inicio = fields.Date('Fecha Inicio BBC 1')
    bbc_fin = fields.Date('Fecha Fin BBC 1')
    bbc_demoras = fields.Integer('Dias Demora')
    bbc_inicio2 = fields.Date('Fecha Inicio BBC 2')
    bbc_fin2 = fields.Date('Fecha Inicio BBC 1')
    bbc_estadia = fields.Integer('Dias Estadia')
    bbc_inicio3 = fields.Date('Fecha Inicio BBC 3')
    bbc_fin3 = fields.Date('Fecha Fin BBC 3')
    fecha_estadia2 = fields.Date('Fecha iInicio Naviera 3')
    fecha_estadia = fields.Date('Fecha Fin Naviera 3')
    dias_demoras = fields.Integer('Dias Demoras')
    dias_estadia = fields.Integer('Dias Estadia')
    dias_almacenaje = fields.Integer('Dia Libre Almacenaje')
    piloto_name = fields.Char('Nombre')
    cel_piloto = fields.Char('Celular')
    placa_piloto = fields.Char('No Placa')
    direccion_entrega = fields.Char('Direccion Entrega Mercaderia')
    seguridad_nombre = fields.Char('Nombre')
    cel_seguridad = fields.Char('Celular')
    observaciones_seg = fields.Text('Observaciones')
    poliza_dua = fields.Char('Poliza DUA')
#aqui qui aqui PruebaJP
    Estatus_Selectividad = fields.Selection([
                    ('A','No Aplica'),
                    ('B','Rojo'),
                    ('C','Verde')
    ],'Estatus Selectivo servicio')
    Asignacion_de_rampa = fields.Char('Asignacion Rampa')
    Gestado_en_lugar = fields.Selection([
                    ('A','Almacen Fiscal'),
                    ('B','Aduana Interna'),
                    ('A','Aereopuerto'),
                    ('B','Frontera'),
                    ('C','Puerto')
    ],'Gestion en: ')
    Inspeccion_fisica_adicional = fields.Selection([
                    ('A','No Aplica'),
                    ('B','Si'),
                    ('C','No')
    ],'Inspeccion adicional   ')
    Entidad_De_inspeccion = fields.Char('Entidad de inspeccion: ')
    fecha_seguro = fields.Date('Fecha de Seguro')
    observaciones_pricing = fields.Text('Observaciones')
    costo_detallado = fields.Text('Costo Detallado')
    f_entrega_cotizacion = fields.Datetime('Fecha Entrega Cotizacion')
    profit_share =  fields.Float('Profit Shared', digits=(12,6))
    h_entrega_cotizacion = fields.Char('Hora Entrega Cotizacion')
    estadia_bbc = fields.Integer('Dias Estadia BBC')
    dia_estadia = fields.Integer('Dias Estadia')
    entrega_hbl = fields.Char('Lugar de Entrega')
    name_competencia = fields.Char('Nombre Competencia')
    direc_origen = fields.Char('Direccion de Origen')
    estadia_libre = fields.Char('Dias Libres Estadia')
    ofrecidos_demoras = fields.Char('Dias Libres Demoras')
    tipo_formato = fields.Many2one('formatos','Tipo de Formatos')
    estado_operaciones = fields.Many2one('so_operaciones','Estado SO operaciones')
    no_mbl = fields.Char('MBL')
    no_hbl = fields.Char('HBL')
    #op_internacional = fields.Many2one('res.partner','Operador Internacional')
    #op_local = fields.Many2one('res.partner','Operador Local')
    op_internacional = fields.Many2one('res.users', string='Operador Internacional', index=True, track_visibility='onchange', track_sequence=2,
                    default=lambda self: self.env.user)
    op_local = fields.Many2one('res.users', string='Operador Local', index=True, track_visibility='onchange', track_sequence=2,
                    default=lambda self: self.env.user)
    envio_cotizacion = fields.Date('Fecha Envio')
    liquidador_conta = fields.Many2one('res.users', string='Responsable Contabilidad', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)
    estado_conta = fields.Many2one('estado_contabilidad','Estado SO Contabilidad')
    responsable_pricing = fields.Many2one('res.users', string='Responsable Pricing', index=True, track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)
    so_subtitulos1 = fields.Char('')
    informar_cliente = fields.Many2one('informar','Como Informar al Ciente')
    estatus_comercial = fields.Many2one('so_status_comercial','Tipo de Incoterms del Cliente',ondelete='cascade',select=True)#fields.Char('Estatus SO Comercial')
    servicio_ventas = fields.Many2one('t_venta','Tipo de Servicio de Venta')
    tipo_traficos1 = fields.Many2one('t_trafico','Tipo de Trafico')
    so_subtitulos = fields.Char('')
    so_comercios = fields.Many2one('so_comercio','Tipo de Venta',ondelete='cascade',select=True)
    so_incotermsclientes = fields.Many2one('so_incotermscliente','Tipo de Incoterms del Cliente',ondelete='cascade',select=True)
    so_incotermservicios = fields.Many2one('so_incotermservicio','Tipo de Incoterms del Cliente',ondelete='cascade',select=True)
    so_mercaderia = fields.Char('Descripción de Mercadería')
    so_ofrecimientos = fields.Many2one('so_ofrecimiento','Ofrecimiento Especial',ondelete='cascade',select=True)
    so_ofrecim = fields.Char('')
    so_taproximado = fields.Char('Tiempo Aproximado de Transito')
    so_validez = fields.Char('Subject')
    so_statusoperacion = fields.Selection([
                    ('C','Cerrado'),
                    ('D','No cerrado')
    ],'Estatus de Operacion')
    so_statusadmon = fields.Selection([
                    ('A','Cerrado'),
                    ('B','No cerrado')
    ],'Estatus Administración')
    so_fpresupuesto = fields.Date('Fecha de Presupuesto')
    so_fseguimiento = fields.Date('Fecha de Seguimiento')
    so_fcierre = fields.Date('Fecha de Cierre de Venta')
    so_fetd = fields.Date('ETD')
    so_feta = fields.Date('ETA')
    so_fentrega = fields.Date('Fecha de Entrega a Cliente')
    so_fpago = fields.Date('Fecha de Pago')
    so_aniocierre = fields.Selection(
        [(num, str(num)) for num in range((datetime.now().year) - 5, (datetime.now().year) + 5)],
        'Anio')
    so_mescierre = fields.Selection([(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                              (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                              (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'), ],
                             string='Mes Muestreo')
    so_tipocambio = fields.Char('Tipo de Cambio')
    so_statusso = fields.Selection([
                    ('E','SO por facturar'),
                    ('F','SO facturada'),
                    ('G','SO pendiente de liquidar'),
                    ('H','SO liquidado operaciones'),
                    ('I','SO liquidado contabilidad'),
    ])
    #Campos inicio pestaña pricing#
    so_contacto_rate = fields.Char('Contact ID')
    so_agente_trabajar = fields.Many2one('res.partner','Agente a Trabajar')
    so_naviera_trabajar = fields.Many2one('res.partner','Naviera a Trabajar')
    so_prov_aduanas = fields.Many2one('res.partner','Proveedor de Aduanas')
    so_prov_transito = fields.Many2one('res.partner','Proveedor Transito Terrestre')
    so_prov_seguridad = fields.Many2one('res.partner','Proveedor Seguridad')
    so_prov_inspeccion = fields.Many2one('res.partner','Proveedor Inspeccion')
    so_prov_seguro = fields.Many2one('res.partner','Proveedor Seguro')
    so_prov_cuadrilla = fields.Many2one('res.partner','Proveedor Cuadrilla')
    so_naviera_aerolinea = fields.Many2one('res.partner','Naviera o Aerolinea')
    so_lugar_entregas = fields.Char('Lugar de Entrega MBL/MAWB')
    so_lugar_entrega = fields.Char('Lugar de Entrega HBL/HAWB')
    servicio_secundario = fields.Char('Servicio Secundario')
    so_tiempo_almacenaje = fields.Char('Tiempo Libre de Almacenaje')
    so_tiempo_demoras = fields.Char('Tiempo libre de Demoras')
    so_cobro_demoras = fields.Char('Inicio de Cobro de Demoras')
    so_dia_almacenaje = fields.Integer('Dias Libres de Almacenaje')
    so_fecha_almacenaje = fields.Date('Fecha Fin Naviera 1')
    so_dia_demora = fields.Integer('Dias Libres de Demoras')
    so_fecha_demora = fields.Date('Fecha Inicio Naviera 1')
    so_dia2_almacenaje = fields.Integer('Dias Libres de Almacenaje')
    so_fecha2_almacenaje = fields.Date('Fecha Fin Naviera 2')
    so_dia2_demoras = fields.Integer('Dias Libres de Demoras')
    so_fecha2_demora = fields.Date('Fecha Fin Naviera 3')
    so_observaciones_pricing = fields.Text('Observaciones')
    so_fecha_tarifa_ventas = fields.Date('Fecha Validez Tarifa Ventas')
    so_fecha_tarifa_origen = fields.Date('Fecha Validez Tarifa Costo Gasto Origen')
    so_fecha_tarifa_destino = fields.Date('Fecha Validez Tarifa Costo Gasto Destino')
    so_fecha_tarifa_inter = fields.Date('Fecha Validez Tarifa Costo Flete Internacional')
    #Campos fin pestaña pricing#
    #Campos inicio pestaña operaciones#
    so_booking = fields.Char('Booking number')
    so_no_buque = fields.Char('No. de Buque')
    puerto_actual_de_zarpe = fields.Many2one('puertos_de_zarpe','Empresa')
    so_no_contenedor = fields.Char('No. de Contenedor')
    Peso_bruto_Kg = fields.Char('Peso Bruto ')
    so_carga_lista = fields.Date('Fecha de Carga Lista')
    so_alerta_zarpa = fields.Date('Fecha de Envio Pre-Alerta Zarpe')
    so_envio_notificacion = fields.Date('Fecha de Envio de Notificacion')
    so_envio_estribo = fields.Date('Fecha de Envio Pre-Alerta Arribo')
    so_no_contenedor_final = fields.Char('No. de Buque')
    so_asegurado = fields.Selection([
                    ('S','Si'),
                    ('N','No'),
                    ('A','No Aplica'),
    ],'Asegurado O')
    so_no_poliza = fields.Char('No. de Poliza')
    so_present_poliza = fields.Date('Fecha de Presentacion de Poliza')
    so_tramitador_puerto = fields.Char('Tramitador del Puerto')
    so_manifestado = fields.Selection([
                    ('SS','Si'),
                    ('NN','No'),
                    ('B','No Aplica'),
    ],'Manifestado O')
    so_no_manifiesto = fields.Char('No. de Manifiesto')
    so_fecha_marchamo = fields.Char('Fecha de Marchamo')
    so_fecha_manifiesto = fields.Date('Fecha de Manifiesto')
    so_courier = fields.Char('Nombre Courier')
    so_tracking = fields.Char('No. Tracking')
    so_datos_proveedor = fields.Many2one('res.partner','Empresa')
    so_contacto1 = fields.Char('Contacto')
    so_direccion3 = fields.Char('Direccion')
    so_telefono = fields.Char('Telefono')
    so_correo = fields.Char('Correo')
    so_no_orden = fields.Char('No. de Orden')
    so_otros = fields.Char('Otros')
    so_ref_proveedor = fields.Char('Referencia Proveedor')
    so_datos_consignatario = fields.Many2one('res.partner','Empresa')
    so_NIT_contacto2 = fields.Char('NIT del Contacto')
    so_FAX_contacto2 = fields.Char('FAX del Contacto')
    so_contacto2 = fields.Char('Contacto')
    so_direccion4 = fields.Char('Direccion')
    so_telefono2 = fields.Char('Telefono')
    so_correo4 = fields.Char('Correo')
    so_no2_orden = fields.Char('No. de orden')
    so_otros2 = fields.Char('Otros')
    so_agente_carga = fields.Char('Profit sugerido')
    so_punto_origen_carga = fields.Char('')
    #Campos grupo mbl#
    so_company_name = fields.Char('Company Name')
    so_direccion2 = fields.Char('Address')
    so_nit3 = fields.Char('TAX ID//RUC//CNPJ//NIT//RIF NO')
    so_telefono3 = fields.Char('Phone Number')
    so_fax3 = fields.Char('Fax number')
    so_contacto3 = fields.Char('Contact Person')
    so_email3 = fields.Char('Email')
    #Campos fin grupo mbl#
    #Campos grupo hbl#
    so_company_name4 = fields.Char('Company Name')
    so_direccion5 = fields.Char('Address')
    so_nit4 = fields.Char('TAX ID//RUC//CNPJ//NIT//RIF NO')
    so_telefono4 = fields.Char('Phone Number')
    so_fax4 = fields.Char('Fax Number')
    so_contacto4 = fields.Char('Contact person')
    #Campos fin grupo hbl#
    #Campos fin grupo hbl2#
    so_pol1 = fields.Char('POL')
    so_pod1 = fields.Char('POD HBL1')
    so_pod2 = fields.Char('POD HBL2')
    so_flete2 = fields.Selection([
                    ('C1','Collect'),
                    ('C2','Prepaid'),
    ])
    #Campos fin grupo mbl2#
    so_pol2 = fields.Char('POL')
    so_pod3 = fields.Char('POD MBL1')
    so_pod4 = fields.Char('POD MBL2')
    so_flete3 = fields.Selection([
                    ('C3','Collect'),
                    ('C4','Prepaid'),
    ])
    #Campos siguen otros campos#
    so_no_hbl = fields.Char('No. HBL')
    so_no_vessel = fields.Char('No. VESSEL/VAPOR')
    so_pre_carriage = fields.Char('Pre-carriage by')
    so_pleace_receipt = fields.Char('Place of receipt by pre-carrier')
    so_routing = fields.Char('Routing and Instructions')
    so_export_carrier = fields.Char('Export Carrier')
    so_loading = fields.Char('Loading Pier/Terminal')
    so_type_move = fields.Char('Type of move')
    so_mrk_contairner = fields.Char('Marks & Nos/Container Nos')
    so_no_pkgs = fields.Char('No. of PKGS')
    so_descripcion_paquetes = fields.Char('Description of Packages and Goods')
    so_gross = fields.Char('Gross Weight')
    so_measurement = fields.Char('Measurement')
    so_freight = fields.Char('Freight & Charges')
    so_basis = fields.Char('Basis')
    so_rate = fields.Char('Rate')
    so_prepaid = fields.Char('Prepaid')
    so_collect = fields.Char('Collect')
    #Campos siguen otros campos "conrte documentation" MBL/MAWB/Carta de parte#
    so_original1 = fields.Boolean('Original')
    so_express1 = fields.Boolean('Express Release')
    so_telex1 = fields.Boolean('Telex')
    so_original2 = fields.Boolean('Original')
    so_express2 = fields.Boolean('Express Release')
    so_telex2 = fields.Boolean('Telex')
    so_mbl5 = fields.Char('No. MBL/MAWB')
    so_observaciones_operaciones = fields.Text('Observaciones')
    #Campos FIN pestaña operaciones#
    #Campos INICIO pestaña ADMINISTRACION#
    so_envio_facturar = fields.Boolean()
    so_facturado3 = fields.Boolean()
    so_no_factura = fields.Char('No. de Factura')
    so_pago_transporte = fields.Many2one('account.payment.term',"Forma Pago Transporte")
    so_observaciones_admon = fields.Text('Observaciones')
    #Campos FIN pestaña ADMINISTRACION#
    #CAMPOS DE DIEGO
    so_cotizacion_contacto = fields.Char('Cotizacion a Nombre de')
    so_cliente = fields.Char('Cliente')
    so_firma = fields.Char('Firma')
    so_tipo_cotizaciones = fields.Many2one('so_tipo_cotizacion','Tipo de cotizacion',ondelete='cascade',select=True)
    so_nivel_prioridades = fields.Many2one('so_nivel_prioridad','Nivel de prioridad',ondelete='cascade',select=True)
    currencys = fields.Many2one('res.currency', string='Tipo de moneda')
    so_valor_mercaderia =  fields.Char('Valor de la mercancia')
    so_tipo_equipos = fields.Many2one('so_tipo_equipo','Tipo de Equipo',ondelete='cascade',select=True)
    so_volumen =  fields.Char('Volumen')
    so_peso =  fields.Char('Peso')
    so_medidas = fields.Char('Medidas')
    so_bultos = fields.Char('Cantidad de bulto')
    so_volumen_cliente =  fields.Char('Volumen del Cliente')
    so_tipo_embalajes = fields.Many2one('so_tipo_embalaje','Tipo de embalaje',ondelete='cascade',select=True)
    so_tipo_mercaderias = fields.Many2one('so_tipo_mercaderia','Tipo de mercancia',ondelete='cascade',select=True)
    so_incluye_aduana = fields.Boolean('Incluye aduana C')
    so_aduana_origen = fields.Boolean('Origen')
    so_aduana_destino = fields.Boolean('Destino')
    so_aduana_ambas = fields.Boolean('Ambas')
    so_tipo_polizas = fields.Many2one('so_tipo_poliza','Tipo de Poliza',ondelete='cascade',select=True)
    so_permisos_especiales = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ])
    so_servicios_especiales = fields.Char('Servicios especiales')
    so_busca_clientes = fields.Many2one('so_busca_cliente','Que Busca el Cliente',ondelete='cascade',select=True)
    so_perioricidades = fields.Many2one('so_perioricidad','Periodicidad',ondelete='cascade',select=True)
    so_frecuencias = fields.Many2one('so_frecuencia','Frecuencia',ondelete='cascade',select=True)
    so_competencias = fields.Many2one('so_competencia','Competencia',ondelete='cascade',select=True)
    so_transporte = fields.Boolean('Transporte c')
    so_transporte_origen = fields.Boolean('Origen')
    so_transporte_destino = fields.Boolean('Destino')
    so_transporte_ambas = fields.Boolean('Ambas')
    so_sobrepeso = fields.Boolean()
    so_peso2 = fields.Char('Peso')
    so_gps = fields.Boolean('GPS')
    so_gps_origen = fields.Boolean('Origen')
    so_gps_destino = fields.Boolean('Destino')
    so_seguridad = fields.Boolean('Seguridad c')
    so_seguridad_origen = fields.Boolean('Origen')
    so_seguridad_destino = fields.Boolean('Destino')
    so_tipo_seguridades = fields.Many2one('so_tipo_seguridad','Tipo de Seguridad',ondelete='cascade',select=True)
    so_seguro_mercaderia = fields.Boolean('Seguro de mercancia')
    so_porcentaje_seguros = fields.Many2one('so_porcentaje_seguro','Porcentaje Seguro',ondelete='cascade',select=True)
    so_cuadrilla = fields.Boolean('Carga y descarga')
    so_cuadrilla_origen = fields.Boolean('Origen')
    so_cuadrilla_destino = fields.Boolean('Destino')
    so_personas = fields.Char('Cantidad de personas')
    so_inspeccion = fields.Boolean('Inspeccion')
    so_inspeccion_origen = fields.Boolean('Origen')
    so_inspeccion_destino = fields.Boolean('Destino')
    so_tipo_inspecciones = fields.Many2one('so_tipo_inspeccion','Tipo de Inspeccion',ondelete='cascade',select=True)
    so_observaciones_comercial = fields.Text('Observaciones')

    sale_invoice_ids = fields.One2many("account.invoice","sale_saleorder_id",string = "Facturas de Venta")
    purchase_invoice_ids = fields.One2many("account.invoice", "purchase_saleorder_id", string = "Facturas de Compra")


    @api.onchange('so_datos_proveedor')
    def onchange_so_datos_proveedor(self):
        if self.so_datos_proveedor:
            self.so_contacto1 = self.so_datos_proveedor.c_encargado_operaciones
            self.so_direccion3 = self.so_datos_proveedor.street
            self.so_correo = self.so_datos_proveedor.email
            self.so_telefono = self.so_datos_proveedor.phone

    @api.onchange('so_datos_consignatario')
    def onchange_so_datos_consignatario(self):
        if self.so_datos_consignatario:
            self.so_contacto2 = self.so_datos_consignatario.c_encargado_operaciones
            self.so_NIT_contacto2 = self.so_datos_consignatario.vat
            self.so_direccion4 =  self.so_datos_consignatario.street
            self.so_telefono2 = self.so_datos_consignatario.phone
            self.so_correo4 = self.so_datos_consignatario.email

    @api.onchange('so_mbl5')
    def onchange_so_mbl5(self):
        if self.so_mbl5:
            self.no_mbl = self.so_mbl5

    @api.onchange('flete_mbl')
    def onchange_flete_mbl(self):
        if self.flete_mbl:
            self.so_flete3 = self.flete_mbl

    @api.onchange('flete_hbl')
    def onchange_flete_hbl(self):
        if self.flete_hbl:
            self.so_flete2 = self.flete_hbl

    @api.onchange('so_dia_almacenaje')
    def onchange_so_dia_almacenaje(self):
        if self.so_dia_almacenaje:
            self.dias_almacenaje = self.so_dia_almacenaje

    @api.onchange('so_no_hbl')
    def onchange_so_no_hbl(self):
        if self.so_no_hbl:
            self.no_hbl = self.so_no_hbl

    @api.onchange('so_no_contenedor')
    def onchange_so_no_contenedor(self):
        if self.so_no_contenedor:
            self.no_contenedor = self.so_no_contenedor

    @api.onchange('so_dia_demora')
    def onchange_so_dia_demora(self):
        if self.so_dia_demora:
            self.dias_demoras = self.so_dia_demora

    @api.onchange('dia_estadia')
    def onchange_dia_estadia(self):
        if self.dia_estadia:
            self.dias_estadia = self.dia_estadia

    @api.onchange('so_dia2_almacenaje')
    def onchange_so_dia2_almacenaje(self):
        if self.so_dia2_almacenaje:
            self.bbc_almacenaje = self.so_dia2_almacenaje

    @api.onchange('so_dia2_demoras')
    def onchange_so_dia2_demoras(self):
        if self.so_dia2_demoras:
            self.bbc_demoras = self.so_dia2_demoras

    @api.onchange('estadia_bbc')
    def onchange_estadia_bbc(self):
        if self.estadia_bbc:
            self.bbc_estadia = self.estadia_bbc

    @api.model
    def create(self,vals):
        if self.env.user.has_group('BBCV.group_operations_all') or self.env.user.has_group('BBCV.group_accounting') or self.env.user.has_group('sales_team.group_sale_salesman'):
            return super(SaleOrder, self).create(vals)
        else:
            partner = self.env['res.partner'].search([('id','=',vals['partner_id'])])
            if partner.user_id.id == self.env.uid:
                return super(SaleOrder, self).create(vals)
            else:
                raise exceptions.ValidationError("No puede generar ordenes para clientes que no tiene asignados.")


class puertos_de_zarpe(models.Model):
    _name = 'puertos_de_zarpe'
    _description = 'puertos_de_zarpe'

    name = fields.Char('Descripcion')


class so_frecuencia1(models.Model):
    _name = 'so_frecuencia1'
    _description = 'Frecuencia'

    name = fields.Char('Descripcion')


class estatus_socomercial(models.Model):
    _name = 'estatus_socomercial'
    _description = 'Estatus comercial'

    name = fields.Char('Descripcion')


class o_cotizacion(models.Model):
    _name = 'o_cotizacion'
    _description = 'Ofrecimiento cotizacion'

    name = fields.Char('Descripcion')


class fac_cliente(models.Model):
    _name = 'fac_cliente'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fac_prov(models.Model):
    _name = 'fac_prov'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fac1(models.Model):
    _name = 'fac1'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fac2(models.Model):
    _name = 'fac2'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fac3(models.Model):
    _name = 'fac3'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fac4(models.Model):
    _name = 'fac4'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class comision_venta(models.Model):
    _name = 'comision_venta'
    _description = 'Comision'

    name = fields.Char('Descripcion')


class comision_pag(models.Model):
    _name = 'comision_pag'
    _description = 'Comision'

    name = fields.Char('Descripcion')


class primer_fac(models.Model):
    _name = 'primer_fac'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class segunda_fac(models.Model):
    _name = 'segunda_fac'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class tercer_fac(models.Model):
    _name = 'tercer_fac'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class cuarta_fac(models.Model):
    _name = 'cuarta_fac'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fact1(models.Model):
    _name = 'fact1'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fact2(models.Model):
    _name = 'fact2'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fact3(models.Model):
    _name = 'fact3'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class fact4(models.Model):
    _name = 'fact4'
    _description = 'Facturacion'

    name = fields.Char('Descripcion')


class liquidacion_gasto(models.Model):
    _name = 'liquidacion_gasto'
    _description = 'Liquidacion gastos'

    name = fields.Char('Descripcion')


class gastos_ri(models.Model):
    _name = 'gastos_ri'
    _description = 'Gastos RI'

    name = fields.Char('Descripcion')


class gasto_demora(models.Model):
    _name = 'gasto_demora'
    _description = 'Gastos demoras'

    name = fields.Char('Descripcion')


class gasto_almacen(models.Model):
    _name = 'gasto_almacen'
    _description = 'Gastos almacenaje'

    name = fields.Char('Descripcion')


class liquidacion_estadia(models.Model):
    _name = 'liquidacion_estadia'
    _description = 'Liquidacion estadia'

    name = fields.Char('Descripcion')


class devolucion_garantia(models.Model):
    _name = 'devolucion_garantia'
    _description = 'Devolucion garantia'

    name = fields.Char('Descripcion')


class formatos(models.Model):
    _name = 'formatos'
    _description = 'Tipo de formatos'

    name = fields.Char('Descripcion')


class so_operaciones(models.Model):
    _name = 'so_operaciones'
    _description = 'Estado SO operaciones'

    name = fields.Char('Descripcion')


class estado_contabilidad(models.Model):
    _name = 'estado_contabilidad'
    _description = 'Estado SO contabilidad'

    name = fields.Char('Descripcion')


class informar(models.Model):
    _name = 'informar'
    _description = 'Como informar al cliente'

    name = fields.Char('Descripcion')


class t_trafico(models.Model):
    _name = 't_trafico'
    _description = 'Tipo de trafico'

    name = fields.Char('Descripcion')


class t_venta(models.Model):
    _name = 't_venta'
    _description = 'Tipo de servicio de venta'

    name = fields.Char('Descripcion')


class so_comercio(models.Model):
    _name = 'so_comercio'
    _description = 'Tipo de comercio'

    name = fields.Char('Descripcion')


class so_incotermscliente(models.Model):
    _name = 'so_incotermscliente'
    _description = 'Tipo de inconterms del cliente'

    name = fields.Char('Descripcion')


class so_incotermservicio(models.Model):
    _name = 'so_incotermservicio'
    _description = 'Tipo de inconterms del servicio'

    name = fields.Char('Descripcion')


class so_ofrecimiento(models.Model):
    _name = 'so_ofrecimiento'
    _description = 'Ofrecimiento especial'

    name = fields.Char('Descripcion')


class so_tipo_cotizacion(models.Model):
    _name = 'so_tipo_cotizacion'
    _description = 'Tipo de cotizacion'

    name = fields.Char('Descripcion')


class so_nivel_prioridad(models.Model):
    _name = 'so_nivel_prioridad'
    _description = 'Nivel de prioridad'

    name = fields.Char('Descripcion')


class currency(models.Model):
    _name = 'currency'
    _description = 'Tipo de moneda'

    name = fields.Char('Descripcion')


class so_tipo_equipo(models.Model):
    _name = 'so_tipo_equipo'
    _description = 'Tipo de equipo'

    name = fields.Char('Descripcion')


class so_tipo_embalaje(models.Model):
    _name = 'so_tipo_embalaje'
    _description = 'Tipo de embalaje'

    name = fields.Char('Descripcion')


class so_tipo_mercaderia(models.Model):
    _name = 'so_tipo_mercaderia'
    _description = 'Tipo de mercaderia'

    name = fields.Char('Descripcion')


class so_tipo_poliza(models.Model):
    _name = 'so_tipo_poliza'
    _description = 'Tipo de poliza'

    name = fields.Char('Descripcion')


class so_busca_cliente(models.Model):
    _name = 'so_busca_cliente'
    _description = 'Que busca el cliente'

    name = fields.Char('Descripcion')


class so_perioricidad(models.Model):
    _name = 'so_perioricidad'
    _description = 'Periodicidad'

    name = fields.Char('Descripcion')


class so_frecuencia(models.Model):
    _name = 'so_frecuencia'
    _description = 'Frecuencia'

    name = fields.Char('Descripcion')


class so_competencia(models.Model):
    _name = 'so_competencia'
    _description = 'Competencia'

    name = fields.Char('Descripcion')


class so_tipo_seguridad(models.Model):
    _name = 'so_tipo_seguridad'
    _description = 'Tipo de seguridad'

    name = fields.Char('Descripcion')


class so_porcentaje_seguro(models.Model):
    _name = 'so_porcentaje_seguro'
    _description = 'Porcentaje de seguro'

    name = fields.Char('Descripcion')


class so_tipo_inspeccion(models.Model):
    _name = 'so_tipo_inspeccion'
    _description = 'Tipo de inspeccion'

    name = fields.Char('Descripcion')

class bbcv_account_invoice(models.Model):
    _inherit = 'account.invoice'

    sale_saleorder_id = fields.Many2one("sale.order","Orden de Venta")
    purchase_saleorder_id = fields.Many2one("sale.order", "Orden de Compra")
