# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _, SUPERUSER_ID
from datetime import datetime


class res_test(models.Model):
    _inherit = "sale.order"

    flete_mbl = fields.Selection([
                    ('C3','Collect'),
                    ('C4','Prepaid')
    ],'Flete mbl p', write=['BBCV.group_pricing_bbc'])
    flete_hbl = fields.Selection([
                    ('C1','Collect'),
                    ('C2','Prepaid')
    ],'Flete hbl p', write=['BBCV.group_pricing_bbc'])
    so_frecuencia = fields.Many2one('so_frecuencia1','Frecuencia so', write=['BBCV.group_comercial_bbc'])
    o_cotizaciones1 = fields.Char('Ofrecimiento especial cotizacion', write=['BBCV.group_comercial_bbc'])
    status_socomercial = fields.Many2one('estatus_socomercial','Estatus comercial', write=['BBCV.group_comercial_bbc'])
    no_contenedor = fields.Char('Contenedor', write=['BBCV.group_operaciones_bbc'])
    o_cotizaciones = fields.Many2one('o_cotizacion','Ofrecimiento especial cotizacion')
    total_prepaid = fields.Char('Total prepaid', write=['BBCV.group_operaciones_bbc'])
    total_collect = fields.Char('Total collect', write=['BBCV.group_operaciones_bbc'])
    date_by = fields.Char('Date by', write=['BBCV.group_operaciones_bbc'])
    on = fields.Char('On', write=['BBCV.group_operaciones_bbc'])
    so_by = fields.Char('By', write=['BBCV.group_operaciones_bbc'])
    observaciones_oper = fields.Text('Observaciones', write=['BBCV.group_operaciones_bbc'])
    place_delivery = fields.Char('Place of delivery by on carrier', write=['BBCV.group_operaciones_bbc'])
    discharge = fields.Char('Port of discharge', write=['BBCV.group_operaciones_bbc'])
    port = fields.Char('Port of loading', write=['BBCV.group_operaciones_bbc'])
    shipper1 = fields.Char('Empresa', write=['BBCV.group_operaciones_bbc'])
    shipper2 = fields.Char('Contacto', write=['BBCV.group_operaciones_bbc'])
    shipper3 = fields.Char('Direccion', write=['BBCV.group_operaciones_bbc'])
    shipper4 = fields.Char('Telefono', write=['BBCV.group_operaciones_bbc'])
    shipper5 = fields.Char('No de orden', write=['BBCV.group_operaciones_bbc'])
    shipper6 = fields.Char('Otros', write=['BBCV.group_operaciones_bbc'])
    shipper7 = fields.Char('Referencia proveedor', write=['BBCV.group_operaciones_bbc'])
    shipper_lading = fields.Char('Booking No', write=['BBCV.group_operaciones_bbc'])
    shipper_booking = fields.Char('Bill of lading No', write=['BBCV.group_operaciones_bbc'])
    shipper_export = fields.Char('Export references', write=['BBCV.group_operaciones_bbc'])
    consignatario1 = fields.Char('Empresa', write=['BBCV.group_operaciones_bbc'])
    consignatario2 = fields.Char('contacto', write=['BBCV.group_operaciones_bbc'])
    consignatario3 = fields.Char('Direccion', write=['BBCV.group_operaciones_bbc'])
    consignatario4 = fields.Char('Telefono', write=['BBCV.group_operaciones_bbc'])
    consignatario5 = fields.Char('No de orden', write=['BBCV.group_operaciones_bbc'])
    consignatario6 = fields.Char('Otros', write=['BBCV.group_operaciones_bbc'])
    consignatario7 = fields.Char('Agente de carga', write=['BBCV.group_operaciones_bbc'])
    consignatario8 = fields.Char('Punto y pais de origen de carga', write=['BBCV.group_operaciones_bbc'])
    consignatario_forwarding = fields.Char('Forwarding', write=['BBCV.group_operaciones_bbc'])
    consignatario_point = fields.Char('Point and country', write=['BBCV.group_operaciones_bbc'])
    consignatario_notify = fields.Char('Notify party', write=['BBCV.group_operaciones_bbc'])
    consignatario_delivery = fields.Char('For delivery', write=['BBCV.group_operaciones_bbc'])
    primerfa = fields.Selection([
                    ('3','No aplica'),
                    ('1','Si'),
                    ('2','No')
    ],'Primer facturacion a1', write=['BBCV.group_contabilidad_bbc'])
    segundafa = fields.Selection([
                    ('3','No aplica'),
                    ('3','Si'),
                    ('4','No')
    ],'Segunda facturacion a2', write=['BBCV.group_contabilidad_bbc'])
    tercerafa = fields.Selection([
                    ('3','No aplica'),
                    ('5','Si'),
                    ('6','No')
    ],'Tercer facturacion a3', write=['BBCV.group_contabilidad_bbc'])
    cuartafa = fields.Selection([
                    ('3','No aplica'),
                    ('7','Si'),
                    ('8','No')
    ],'cuarta facturacion a4', write=['BBCV.group_contabilidad_bbc'])
    no_fact1 = fields.Char('No de factura a1', write=['BBCV.group_contabilidad_bbc'])
    no_fact2 = fields.Char('No de factura a2', write=['BBCV.group_contabilidad_bbc'])
    no_fact3 = fields.Char('No de factura a3', write=['BBCV.group_contabilidad_bbc'])
    no_fact4 = fields.Char('No de factura a4', write=['BBCV.group_contabilidad_bbc'])
    document = fields.Char('No de documento a1', write=['BBCV.group_contabilidad_bbc'])
    document1 = fields.Char('No de documento a2', write=['BBCV.group_contabilidad_bbc'])
    oc1 = fields.Char('No de OC a1', write=['BBCV.group_contabilidad_bbc'])
    oc2 = fields.Char('No de OC a2', write=['BBCV.group_contabilidad_bbc'])
    oc3 = fields.Char('No de OC a3', write=['BBCV.group_contabilidad_bbc'])
    oc4 = fields.Char('No de OC a4', write=['BBCV.group_contabilidad_bbc'])
    factura9 = fields.Many2one('fac_cliente','Facturacion', write=['BBCV.group_contabilidad_bbc'])
    factura10 = fields.Many2one('fac_prov','Tipo de factura del proveedor', write=['BBCV.group_contabilidad_bbc'])
    factura11 = fields.Many2one('fac1',' OC 1 facturacion', write=['BBCV.group_contabilidad_bbc'])
    factura12 = fields.Many2one('fac2','OC 2 facturacion', write=['BBCV.group_contabilidad_bbc'])
    factura13 = fields.Many2one('fac3','OC 3 facturacion', write=['BBCV.group_contabilidad_bbc'])
    factura14 = fields.Many2one('fac4','OC 4 facturacion', write=['BBCV.group_contabilidad_bbc'])
    comision_ventas = fields.Many2one('comision_venta','Comisiones pagadas de ventas', write=['BBCV.group_contabilidad_bbc'])
    comision_pagadas = fields.Many2one('comision_pag','Comisiones pagadas de operaciones', write=['BBCV.group_contabilidad_bbc'])
    observaciones_facturacion = fields.Text('Observaciones', write=['BBCV.group_operaciones_bbc'])
    factura1 = fields.Many2one('primer_fac','Primer facturacion o1', write=['BBCV.group_operaciones_bbc'])
    factura2 = fields.Many2one('segunda_fac','Segunda facturacion o2', write=['BBCV.group_operaciones_bbc'])
    factura3 = fields.Many2one('tercer_fac','Tercer facturacion o3', write=['BBCV.group_operaciones_bbc'])
    factura4 = fields.Many2one('cuarta_fac','Cuarta facturacion 04', write=['BBCV.group_operaciones_bbc'])
    factura5 = fields.Many2one('fact1','Orden de compra 1er facturacion', write=['BBCV.group_operaciones_bbc'])
    factura6 = fields.Many2one('fact2','Orden de compra 2da facturacion', write=['BBCV.group_operaciones_bbc'])
    factura7 = fields.Many2one('fact3','Orden de compra 3ra facturacion', write=['BBCV.group_operaciones_bbc'])
    factura8 = fields.Many2one('fact4','Orden de compra 4ta facturacion', write=['BBCV.group_operaciones_bbc'])
    liquidaciones = fields.Many2one('liquidacion_gasto','Titulo sin filtro')
    gastosri = fields.Many2one('gastos_ri','Liquidacion gastos RI', write=['BBCV.group_operaciones_bbc'])
    gastos_demoras = fields.Many2one('gasto_demora','Liquidacion gastos demoras', write=['BBCV.group_operaciones_bbc'])
    gastos_almacenajes = fields.Many2one('gasto_almacen','Liquidacion gastos almacenaje', write=['BBCV.group_operaciones_bbc'])
    liquidaciones_estadias = fields.Many2one('liquidacion_estadia','Liquidacion de gastos estadias', write=['BBCV.group_operaciones_bbc'])
    fecha_devolucion = fields.Date('Fecha devolucion del contenedor', write=['BBCV.group_operaciones_bbc'])
    devoluciones_garantias = fields.Many2one('devolucion_garantia','Devolucion de depositos en garantia', write=['BBCV.group_operaciones_bbc'])
    fecha_finalizacion = fields.Date('Fecha finalizacion de la operacion', write=['BBCV.group_operaciones_bbc'])
    valor_estadias = fields.Char('valor estadias de transportes', write=['BBCV.group_operaciones_bbc'])
    bbc_almacenaje = fields.Integer('Dia almacenaje', write=['BBCV.group_operaciones_bbc'])
    bbc_inicio = fields.Date('Fecha inicio obbc1', write=['BBCV.group_operaciones_bbc'])
    bbc_fin = fields.Date('Fecha fin obbc1', write=['BBCV.group_operaciones_bbc'])
    bbc_demoras = fields.Integer('Dias demoras', write=['BBCV.group_operaciones_bbc'])
    bbc_inicio2 = fields.Date('Fecha inicio obbc2', write=['BBCV.group_operaciones_bbc'])
    bbc_fin2 = fields.Date('Fecha inicio obbc1', write=['BBCV.group_operaciones_bbc'])
    bbc_estadia = fields.Integer('Dias estadia', write=['BBCV.group_operaciones_bbc'])
    bbc_inicio3 = fields.Date('Fecha inicio obbc3', write=['BBCV.group_operaciones_bbc'])
    bbc_fin3 = fields.Date('Fecha fin obbc3', write=['BBCV.group_operaciones_bbc'])
    fecha_estadia2 = fields.Date('Fecha inicio onaviera3', write=['BBCV.group_operaciones_bbc'])
    fecha_estadia = fields.Date('Fecha fin onaviera3', write=['BBCV.group_operaciones_bbc'])
    dias_demoras = fields.Integer('Dias demoras', write=['BBCV.group_operaciones_bbc'])
    dias_estadia = fields.Integer('Dias estadia', write=['BBCV.group_operaciones_bbc'])
    dias_almacenaje = fields.Integer('Dia libre almacenaje', write=['BBCV.group_operaciones_bbc'])
    piloto_name = fields.Char('Nombre', write=['BBCV.group_operaciones_bbc'])
    cel_piloto = fields.Char('Cel', write=['BBCV.group_operaciones_bbc'])
    placa_piloto = fields.Char('no placa', write=['BBCV.group_operaciones_bbc'])
    direccion_entrega = fields.Char('Direccion entrega merca', write=['BBCV.group_operaciones_bbc'])
    seguridad_nombre = fields.Char('Nombre', write=['BBCV.group_operaciones_bbc'])
    cel_seguridad = fields.Char('Cel', write=['BBCV.group_operaciones_bbc'])
    observaciones_seg = fields.Text('', write=['BBCV.group_operaciones_bbc'])
    poliza_dua = fields.Char('Poliza DUA', write=['BBCV.group_operaciones_bbc'])
#aqui qui aqui PruebaJP
    Estatus_Selectividad = fields.Selection([
                    ('A','No Aplica'),
                    ('B','Rojo'),
                    ('C','Verde')
    ],'Estatus Selectivo servicio', write=['BBCV.group_operaciones_bbc'])
    Asignacion_de_rampa = fields.Char('Asignacion Rampa', write=['BBCV.group_operaciones_bbc'])
    Gestado_en_lugar = fields.Selection([
                    ('A','Almacen Fiscal'),
                    ('B','Aduana Interna'),
                    ('A','Aereopuerto'),
                    ('B','Frontera'),
                    ('C','Puerto')
    ],'Gestion en: ', write=['BBCV.group_operaciones_bbc'])
    Inspeccion_fisica_adicional = fields.Selection([
                    ('A','No Aplica'),
                    ('B','Si'),
                    ('C','No')
    ],'Inspeccion adicional   ', write=['BBCV.group_operaciones_bbc'])
    Entidad_De_inspeccion = fields.Char('Entidad de inspeccion: ', write=['BBCV.group_operaciones_bbc'])
    fecha_seguro = fields.Date('Fecha de seguro', write=['BBCV.group_operaciones_bbc'])
    observaciones_pricing = fields.Text('Observaciones', write=['BBCV.group_pricing_bbc'])
    costo_detallado = fields.Text('Costo detallado', write=['BBCV.group_pricing_bbc'])
    f_entrega_cotizacion = fields.Date('Fecha entrega cotizacion', write=['BBCV.group_pricing_bbc'])
    profit_share =  fields.Float('Profit Shared', digits=(12,6), write=['BBCV.group_pricing_bbc'])
    h_entrega_cotizacion = fields.Char('Hora entrega cotizacion', write=['BBCV.group_pricing_bbc'])
    estadia_bbc = fields.Integer('Dias estadia', write=['BBCV.group_pricing_bbc'])
    dia_estadia = fields.Integer('Dias estadia', write=['BBCV.group_pricing_bbc'])
    entrega_hbl = fields.Char('Lugar de entrega')
    name_competencia = fields.Char('Nombre competencia', write=['BBCV.group_comercial_bbc'])
    direc_origen = fields.Char('Direccion de origen', write=['BBCV.group_comercial_bbc'])
    estadia_libre = fields.Char('Dias libres estadia', write=['BBCV.group_comercial_bbc'])
    ofrecidos_demoras = fields.Char('Dias libres demoras', write=['BBCV.group_comercial_bbc'])
    tipo_formato = fields.Many2one('formatos','Tipo de formatos', write=['BBCV.group_comercial_bbc'])
    liquidador_oper = fields.Many2one('res.partner','Liquidador operaciones', write=['BBCV.group_operaciones_bbc'])
    estado_operaciones = fields.Many2one('so_operaciones','Estado SO operaciones', write=['BBCV.group_operaciones_bbc'])
    no_mbl = fields.Char('MBL', write=['BBCV.group_operaciones_bbc'])
    no_hbl = fields.Char('HBL', write=['BBCV.group_operaciones_bbc'])
    op_internacional = fields.Many2one('res.partner','Operador internacional', write=['BBCV.group_operaciones_bbc'])
    op_local = fields.Many2one('res.partner','Operador local', write=['BBCV.group_operaciones_bbc'])
    envio_cotizacion = fields.Date('Fecha envio')
    liquidador_conta = fields.Many2one('res.partner','Liquidador contabilidad', write=['BBCV.group_contabilidad_bbc'])
    estado_conta = fields.Many2one('estado_contabilidad','Estado SO contabilidad', write=['BBCV.group_contabilidad_bbc'])
    responsable_pricing = fields.Many2one('res.partner','Responsable pricing', write=['BBCV.group_pricing_bbc'])
    so_subtitulos1 = fields.Char('')
    informar_cliente = fields.Many2one('informar','Como informar al ciente', write=['BBCV.group_comercial_bbc'])
    estatus_comercial = fields.Char('Estatus SO comercial')
    servicio_ventas = fields.Many2one('t_venta','Tipo de servicio de venta', write=['BBCV.group_comercial_bbc'])
    tipo_traficos1 = fields.Many2one('t_trafico','Tipo de trafico', write=['BBCV.group_comercial_bbc'])
    so_subtitulos = fields.Char('')
    so_comercios = fields.Many2one('so_comercio','Tipo de venta',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_incotermsclientes = fields.Many2one('so_incotermscliente','Tipo de incoterms del cliente',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_incotermservicios = fields.Many2one('so_incotermservicio','Tipo de incoterms del cliente',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_mercaderia = fields.Char('Descripción de mercadería', write=['BBCV.group_comercial_bbc'])
    so_ofrecimientos = fields.Many2one('so_ofrecimiento','Ofrecimiento especial',ondelete='cascade',select=True)
    so_ofrecim = fields.Char('', write=['BBCV.group_comercial_bbc'])
    so_taproximado = fields.Char('Tiempo aproximado de transito')
    so_validez = fields.Char('Subject')
    so_statusoperacion = fields.Selection([
                    ('C','Cerrado'),
                    ('D','No cerrado')
    ],'Estatus de operacion', write=['BBCV.group_operaciones_bbc'])
    so_statusadmon = fields.Selection([
                    ('A','Cerrado'),
                    ('B','No cerrado')
    ],'Estatus admon', write=['BBCV.group_pricing_bbc'])
    so_fpresupuesto = fields.Date('Fecha de presupuesto')
    so_fseguimiento = fields.Date('Fecha de seguimiento')
    so_fcierre = fields.Date('Fecha de cierre de venta')
    so_fetd = fields.Date('ETD', write=['BBCV.group_operaciones_bbc'])
    so_feta = fields.Date('ETA', write=['BBCV.group_operaciones_bbc'])
    so_fentrega = fields.Date('Fecha de entrega a cliente', write=['BBCV.group_operaciones_bbc'])
    so_fpago = fields.Date('Fecha de pago', write=['BBCV.group_contabilidad_bbc'])
    so_aniocierre = fields.Selection(
        [(num, str(num)) for num in range((datetime.now().year) - 5, (datetime.now().year) + 5)],
        'Año')
    so_mescierre = fields.Selection([(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                              (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                              (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'), ],
                             string='Mes Muestreo')
    so_tipocambio = fields.Char('Tipo de cambio', write=['BBCV.group_pricing_bbc'])
    so_statusso = fields.Selection([
                    ('E','SO por facturar'),
                    ('F','SO facturada'),
                    ('G','SO pendiente de liquidar'),
                    ('H','SO liquidado operaciones'),
                    ('I','SO liquidado contabilidad'),
    ])
    #Campos inicio pestaña pricing#
    so_contacto_rate = fields.Char('Contact ID', write=['BBCV.group_pricing_bbc'])
    so_agente_trabajar = fields.Many2one('res.partner','Agente a trabajar', write=['BBCV.group_pricing_bbc'])
    so_naviera_trabajar = fields.Many2one('res.partner','Naviera a trabajar', write=['BBCV.group_pricing_bbc'])
    so_prov_aduanas = fields.Many2one('res.partner','Proveedor de aduanas', write=['BBCV.group_pricing_bbc'])
    so_prov_transito = fields.Many2one('res.partner','Proveedor transito terrestre', write=['BBCV.group_pricing_bbc'])
    so_prov_seguridad = fields.Many2one('res.partner','Proveedor seguridad', write=['BBCV.group_pricing_bbc'])
    so_prov_inspeccion = fields.Many2one('res.partner','Proveedor inspeccion', write=['BBCV.group_pricing_bbc'])
    so_prov_seguro = fields.Many2one('res.partner','Proveedor seguro', write=['BBCV.group_pricing_bbc'])
    so_prov_cuadrilla = fields.Many2one('res.partner','Proveedor vuadrilla', write=['BBCV.group_pricing_bbc'])
    so_naviera_aerolinea = fields.Many2one('res.partner','Naviera o aerolinea')
    so_lugar_entregas = fields.Char('Lugar de entrega MBL/MAWB', write=['BBCV.group_pricing_bbc'])
    so_lugar_entrega = fields.Char('Lugar de entrega HBL/HAWB', write=['BBCV.group_pricing_bbc'])
    servicio_secundario = fields.Char('Servicio secundario', write=['BBCV.group_pricing_bbc'])
    so_tiempo_almacenaje = fields.Char('Tiempo libre de almacenaje')
    so_tiempo_demoras = fields.Char('Tiempo libre de demoras')
    so_cobro_demoras = fields.Char('Inicio de cobro de demoras')
    #'so_dia_almacenajee = fields.Char('Dias libres de almacenaje')
    so_dia_almacenaje = fields.Integer('Dias libres de almacenaje', write=['BBCV.group_pricing_bbc'])
    so_fecha_almacenaje = fields.Date('Fecha fin onaviera1', write=['BBCV.group_operaciones_bbc'])
    so_dia_demora = fields.Integer('Dias libres de demoras', write=['BBCV.group_pricing_bbc'])
    so_fecha_demora = fields.Date('Fecha inicio onaviera1', write=['BBCV.group_operaciones_bbc'])
    so_dia2_almacenaje = fields.Integer('Dias libres de almacenaje', write=['BBCV.group_pricing_bbc'])
    so_fecha2_almacenaje = fields.Date('Fecha fin onaviera2', write=['BBCV.group_operaciones_bbc'])
    so_dia2_demoras = fields.Integer('Dias libres de demoras', write=['BBCV.group_pricing_bbc'])
    so_fecha2_demora = fields.Date('Fecha fin onaviera3', write=['BBCV.group_operaciones_bbc'])
    so_observaciones_pricing = fields.Text('Observaciones', write=['BBCV.group_pricing_bbc'])
    so_fecha_tarifa_ventas = fields.Date('Fecha validez tarifa ventas', write=['BBCV.group_pricing_bbc'])
    so_fecha_tarifa_origen = fields.Date('Fecha validez tarifa costo gasto origen', write=['BBCV.group_pricing_bbc'])
    so_fecha_tarifa_destino = fields.Date('Fecha validez tarifa costo gasto destino', write=['BBCV.group_pricing_bbc'])
    so_fecha_tarifa_inter = fields.Date('Fecha validez tarifa costo flete internacional', write=['BBCV.group_pricing_bbc'])
    #Campos fin pestaña pricing#
    #Campos inicio pestaña operaciones#
    so_booking = fields.Char('Booking number')
    so_no_buque = fields.Char('No. de buque', write=['BBCV.group_operaciones_bbc'])
    puerto_actual_de_zarpe = fields.Many2one('puertos_de_zarpe','Empresa')
    so_no_contenedor = fields.Char('No. de contenedor', write=['BBCV.group_operaciones_bbc'])
    Peso_bruto_Kg = fields.Char('Peso Bruto ', write=['BBCV.group_operaciones_bbc'])
    so_carga_lista = fields.Date('Fecha de carga lista', write=['BBCV.group_operaciones_bbc'])
    so_alerta_zarpa = fields.Date('Fecha de envio pre-alerta zarpa', write=['BBCV.group_operaciones_bbc'])
    so_envio_notificacion = fields.Date('Fecha de envio de notificacion', write=['BBCV.group_operaciones_bbc'])
    so_envio_estribo = fields.Date('Fecha de envio pre-alerta arribo', write=['BBCV.group_operaciones_bbc'])
    so_no_contenedor_final = fields.Char('No. de Buque ', write=['BBCV.group_operaciones_bbc'])
    so_asegurado = fields.Selection([
                    ('S','Si'),
                    ('N','No'),
                    ('A','No aplica'),
    ],'Asegurado O', write=['BBCV.group_operaciones_bbc'])
    so_no_poliza = fields.Char('No. de poliza', write=['BBCV.group_operaciones_bbc'])
    so_present_poliza = fields.Date('Fecha de presentacion de poliza', write=['BBCV.group_operaciones_bbc'])
    so_tramitador_puerto = fields.Char('Tramitador del puerto', write=['BBCV.group_operaciones_bbc'])
    so_manifestado = fields.Selection([
                    ('SS','Si'),
                    ('NN','No'),
                    ('B','No aplica'),
    ],'Manifestado O', write=['BBCV.group_operaciones_bbc'])
    so_no_manifiesto = fields.Char('No. de manifiesto', write=['BBCV.group_operaciones_bbc'])
    so_fecha_marchamo = fields.Char('Fecha de marchamo', write=['BBCV.group_operaciones_bbc'])
    so_fecha_manifiesto = fields.Date('Fecha de manifiesto', write=['BBCV.group_operaciones_bbc'])
    so_courier = fields.Char('Nombre courier', write=['BBCV.group_operaciones_bbc'])
    so_tracking = fields.Char('No. tracking', write=['BBCV.group_operaciones_bbc'])
    so_datos_proveedor = fields.Many2one('res.partner','Empresa')
    so_contacto1 = fields.Char('Contacto')
    so_direccion3 = fields.Char('Direccion')
    so_telefono = fields.Char('Telefono')
    so_correo = fields.Char('Correo')
    so_no_orden = fields.Char('No. de orden')
    so_otros = fields.Char('Otros')
    so_ref_proveedor = fields.Char('Referencia proveedor')
    so_datos_consignatario = fields.Many2one('res.partner','Empresa')
    so_NIT_contacto2 = fields.Char('Nit del Contacto')
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
    so_company_name = fields.Char('Company name', write=['BBCV.group_pricing_bbc'])
    so_direccion2 = fields.Char('Address', write=['BBCV.group_pricing_bbc'])
    so_nit3 = fields.Char('TAX ID//RUC//CNPJ//NIT//RIF NO', write=['BBCV.group_pricing_bbc'])
    so_telefono3 = fields.Char('Phone number', write=['BBCV.group_pricing_bbc'])
    so_fax3 = fields.Char('Fax number', write=['BBCV.group_pricing_bbc'])
    so_contacto3 = fields.Char('Contact person', write=['BBCV.group_pricing_bbc'])
    so_email3 = fields.Char('Email address', write=['BBCV.group_pricing_bbc'])
    #Campos fin grupo mbl#
    #Campos grupo hbl#
    so_company_name4 = fields.Char('Company name')
    so_direccion5 = fields.Char('Address')
    so_nit4 = fields.Char('TAX ID//RUC//CNPJ//NIT//RIF NO')
    so_telefono4 = fields.Char('Phone number')
    so_fax4 = fields.Char('Fax number')
    so_contacto4 = fields.Char('Contact person')
    #Campos fin grupo hbl#
    #Campos fin grupo hbl2#
    so_pol1 = fields.Char('POL', write=['BBCV.group_operaciones_bbc'])
    so_pod1 = fields.Char('POD HBL1', write=['BBCV.group_operaciones_bbc'])
    so_pod2 = fields.Char('POD HBL2', write=['BBCV.group_operaciones_bbc'])
    so_flete2 = fields.Selection([
                    ('C1','Collect'),
                    ('C2','Prepaid'),
    ], write=['BBCV.group_operaciones_bbc'])
    #Campos fin grupo mbl2#
    so_pol2 = fields.Char('POL', write=['BBCV.group_operaciones_bbc'])
    so_pod3 = fields.Char('POD MBL1', write=['BBCV.group_operaciones_bbc'])
    so_pod4 = fields.Char('POD MBL2', write=['BBCV.group_operaciones_bbc'])
    so_flete3 = fields.Selection([
                    ('C3','Collect'),
                    ('C4','Prepaid'),
    ], write=['BBCV.group_operaciones_bbc'])
    #Campos siguen otros campos#
    so_no_hbl = fields.Char('No. HBL', write=['BBCV.group_operaciones_bbc'])
    so_no_vessel = fields.Char('No. VESSEL/VAPOR')
    so_pre_carriage = fields.Char('Pre-carriage by', write=['BBCV.group_operaciones_bbc'])
    so_pleace_receipt = fields.Char('Pleace of receipt by pre-carrier', write=['BBCV.group_operaciones_bbc'])
    so_routing = fields.Char('Routing and instructions', write=['BBCV.group_operaciones_bbc'])
    so_export_carrier = fields.Char('Export carrier', write=['BBCV.group_operaciones_bbc'])
    so_loading = fields.Char('Loading pier/terminal', write=['BBCV.group_operaciones_bbc'])
    so_type_move = fields.Char('Type of move', write=['BBCV.group_operaciones_bbc'])
    so_mrk_contairner = fields.Char('Marks & Nos/Container Nos', write=['BBCV.group_operaciones_bbc'])
    so_no_pkgs = fields.Char('No. of PKGS', write=['BBCV.group_operaciones_bbc'])
    so_descripcion_paquetes = fields.Char('Description of packages and goods', write=['BBCV.group_operaciones_bbc'])
    so_gross = fields.Char('Gross weight', write=['BBCV.group_operaciones_bbc'])
    so_measurement = fields.Char('Measurement', write=['BBCV.group_operaciones_bbc'])
    so_freight = fields.Char('Freight & charges', write=['BBCV.group_operaciones_bbc'])
    so_basis = fields.Char('Basis', write=['BBCV.group_operaciones_bbc'])
    so_rate = fields.Char('Rate', write=['BBCV.group_operaciones_bbc'])
    so_prepaid = fields.Char('Prepaid', write=['BBCV.group_operaciones_bbc'])
    so_collect = fields.Char('Collect', write=['BBCV.group_operaciones_bbc'])
    #Campos siguen otros campos "conrte documentation" MBL/MAWB/Carta de parte#
    so_original1 = fields.Boolean('Original', write=['BBCV.group_operaciones_bbc'])
    so_express1 = fields.Boolean('Express release', write=['BBCV.group_operaciones_bbc'])
    so_telex1 = fields.Boolean('Telex', write=['BBCV.group_operaciones_bbc'])
    so_original2 = fields.Boolean('Original', write=['BBCV.group_operaciones_bbc'])
    so_express2 = fields.Boolean('Express release', write=['BBCV.group_operaciones_bbc'])
    so_telex2 = fields.Boolean('Telex', write=['BBCV.group_operaciones_bbc'])
    so_mbl5 = fields.Char('No. MBL/MAWB', write=['BBCV.group_operaciones_bbc'])
    so_observaciones_operaciones = fields.Text('Observaciones', write=['BBCV.group_operaciones_bbc'])
    #Campos FIN pestaña operaciones#
    #Campos INICIO pestaña ADMINISTRACION#
    so_envio_facturar = fields.Selection([
                    ('sss','Si'),
                    ('nnn','No'),
    ])
    so_facturado3 = fields.Selection([
                    ('ssss','Si'),
                    ('nnnn','No'),
    ])
    so_no_factura = fields.Char('No. de factura')
    so_pago_cliente = fields.Selection([
                    ('contado','Contado'),
                    ('8','8'),
                    ('15','15'),
                    ('30','30'),
                    ('45','45'),
                    ('46','Segun ficha del cliente'),
    ],'Tiempo de pago del cliente', write=['BBCV.group_contabilidad_bbc'])
    so_pago_transporte = fields.Selection([
                    ('conta','Contado'),
                    ('p','8'),
                    ('q','15'),
                    ('t','30'),
                    ('cua','45'),
                    ('47','Segun ficha del proveedor'),
    ],'Tiempo de pago del transporte principal', write=['BBCV.group_contabilidad_bbc'])
    so_observaciones_admon = fields.Text('Observaciones', write=['BBCV.group_contabilidad_bbc'])
    #Campos FIN pestaña ADMINISTRACION#
    #CAMPOS DE DIEGO
    so_cotizacion_contacto = fields.Char('Cotizacion a nombre de', write=['BBCV.group_comercial_bbc'])
    so_cliente = fields.Char('Cliente', write=['BBCV.group_comercial_bbc'])
    so_firma = fields.Char('Firma', write=['BBCV.group_comercial_bbc'])
    so_tipo_cotizaciones = fields.Many2one('so_tipo_cotizacion','Tipo de cotizacion',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_nivel_prioridades = fields.Many2one('so_nivel_prioridad','Nivel de prioridad',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    currencys = fields.Many2one('res.currency', string='Tipo de moneda')
    
    so_valor_mercaderia =  fields.Char('Valor de la mercancia', write=['BBCV.group_comercial_bbc'])
    so_tipo_equipos = fields.Many2one('so_tipo_equipo','Tipo de Equipo',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_volumen =  fields.Char('Volumen', write=['BBCV.group_comercial_bbc'])
    so_peso =  fields.Char('Peso')
    so_medidas = fields.Char('Medidas', write=['BBCV.group_comercial_bbc'])
    so_bultos = fields.Char('Cantidad de bulto', write=['BBCV.group_comercial_bbc'])
    so_volumen_cliente =  fields.Char('Volumen del Cliente', write=['BBCV.group_comercial_bbc'])
    so_tipo_embalajes = fields.Many2one('so_tipo_embalaje','Tipo de embalaje',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_tipo_mercaderias = fields.Many2one('so_tipo_mercaderia','Tipo de mercancia',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_incluye_aduana = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Incluye aduana c', write=['BBCV.group_comercial_bbc'])
    so_aduana_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_aduana_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_aduana_ambas = fields.Boolean('Ambas', write=['BBCV.group_comercial_bbc'])
    so_tipo_polizas = fields.Many2one('so_tipo_poliza','Tipo de Poliza',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_permisos_especiales = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ], write=['BBCV.group_comercial_bbc'])
    so_servicios_especiales = fields.Char('Servicios especiales', write=['BBCV.group_comercial_bbc'])
    so_busca_clientes = fields.Many2one('so_busca_cliente','Que busca el cliente',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_perioricidades = fields.Many2one('so_perioricidad','Periodicidad',ondelete='cascade',select=True)
    so_frecuencias = fields.Many2one('so_frecuencia','Frecuencia',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_competencias = fields.Many2one('so_competencia','Competencia',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_transporte = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Transporte c', write=['BBCV.group_comercial_bbc'])
    so_transporte_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_transporte_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_transporte_ambas = fields.Boolean('Ambas', write=['BBCV.group_comercial_bbc'])
    so_sobrepeso = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ], write=['BBCV.group_comercial_bbc'])
    so_peso2 = fields.Char('Peso', write=['BBCV.group_comercial_bbc'])
    so_gps = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ], write=['BBCV.group_comercial_bbc'])
    so_gps_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_gps_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_seguridad = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Seguridad c', write=['BBCV.group_comercial_bbc'])
    so_seguridad_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_seguridad_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_tipo_seguridades = fields.Many2one('so_tipo_seguridad','Tipo de Seguridad',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_seguro_mercaderia = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Seguro de mercancia', write=['BBCV.group_comercial_bbc'])
    so_porcentaje_seguros = fields.Many2one('so_porcentaje_seguro','Porcentaje Seguro',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_cuadrilla = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Carga y descarga', write=['BBCV.group_comercial_bbc'])
    so_cuadrilla_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_cuadrilla_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_personas = fields.Char('Cantidad de personas', write=['BBCV.group_comercial_bbc'])
    so_inspeccion = fields.Selection([
                    ('si','Si'),
                    ('no','No'),
    ],'Inspeccion', write=['BBCV.group_comercial_bbc'])
    so_inspeccion_origen = fields.Boolean('Origen', write=['BBCV.group_comercial_bbc'])
    so_inspeccion_destino = fields.Boolean('Destino', write=['BBCV.group_comercial_bbc'])
    so_tipo_inspecciones = fields.Many2one('so_tipo_inspeccion','Tipo de inspeccion',ondelete='cascade',select=True, write=['BBCV.group_comercial_bbc'])
    so_observaciones_comercial = fields.Text('Observaciones', write=['BBCV.group_comercial_bbc'])
    #'servicio_venta = fields.Many2one('servicio_ventas','Tipo de servicio de venta'),
    #'tipo_trafico = fields.many2one('tipos_trafico','Tipo de trafico')

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