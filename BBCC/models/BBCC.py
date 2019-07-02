# -*- coding: utf-8 -*-


from odoo import api, exceptions, fields, models, _, SUPERUSER_ID


class res_test(models.Model):
    _inherit = "res.partner"

    p_tipo_base = fields.Many2one('tipo_base2', 'Tipo de base')
    ycomercios = fields.Many2one('ycomercio', 'proveedor')
    yservicios = fields.Many2one('yservicio', 'proveedor')
    origen_servicio = fields.Many2one('res.country', 'Pais de origen')
    c_observaciones = fields.Text('Observaciones')
    c_inactivo = fields.Many2one('inactivo', 'Inactivo')
    c_base = fields.Many2one('tipo_base', 'Tipo de base')
    c_busca = fields.Many2one('busca_cliente', 'Que busca el cliente')
    c_internacional = fields.Many2one('o_internacional', 'Operador internacional')
    c_local = fields.Many2one('o_local', 'Operador local')
    estado_cliente = fields.Many2one('estados_cliente', 'Estatus del Cliente', ondelete='cascade', select=True)
    tipos_cliente = fields.Many2one('tipo_cliente', 'Tipo de Cliente', ondelete='cascade', select=True)
    otro_servicio = fields.Char('Otro tipo de servicio') 
    activ_economica = fields.Many2one('act_economica', 'Actividad economica', ondelete='cascade', select=True)
    pais_servicios = fields.Many2one('res.country', 'Pais de origen de servicios')
    trafic_manejar = fields.Many2one('trafico_manejar', 'Tipo de trafico a manejar')
    comercio_clientes = fields.Many2one('comercio_cliente', 'Tipo de comercio del cliente', ondelete='cascade', select=True)
    servicio_clientes = fields.Many2one('servicio_cliente', 'Tipo de servicio del cliente', ondelete='cascade', select=True)
    regimen = fields.Selection([
            ('1', 'Sobre utilidades lucrativas 25%'),
            ('2', 'Opcional simplificado 7%'),
            ('3', 'Pequeño contribuyente'),
            ('4', 'Renta de trabajo')
        ])
    f_factura = fields.Many2one('f_facturar', '¿Cuando se manda a facturar?', ondelete='cascade', select=True)
    f_internacion = fields.Many2one('f_internacional', 'Tipo factura servicio internacional', ondelete='cascade', select=True)
    f_lokal = fields.Many2one('f_local', 'Tipo factura servicio local', ondelete='cascade', select=True)
    f_otros = fields.Char('Otros tipos de facturacion')
    entrega_facturas = fields.Char('Direccion de entrega de factura')
    r_facturas = fields.Many2one('r_factura', 'Dia de recepcion de factura', ondelete='cascade', select=True)
    horario_recepcion = fields.Char('Horario de recepcion de factura')
    i_cobro = fields.Char('Instrucciones para cobro')
    h_pago = fields.Char('Horario de pago')
    dia_pagos = fields.Many2one('dia_pago', 'Dia de pago', ondelete='cascade', select=True)
    proveedores_para = fields.Many2one('proveedor_para', 'Proveedor para', ondelete='cascade', select=True)
    pais_proveedores = fields.Many2one('res.country', 'Pais proveedor')
    estatus_proveedores = fields.Many2one('estatus_proveedor', 'Estatus de proveedor', ondelete='cascade', select=True)
    actividad_proveedores = fields.Many2one('act_proveedor', 'Actividad de proveedor', ondelete='cascade', select=True)
    admon_proveedores = fields.Many2one('admon_proveedor', 'Proveedor de administracion', ondelete='cascade', select=True)
    oper_proveedores = fields.Many2one('oper_proveedor', 'Proveedor de operaciones', ondelete='cascade', select=True)
    comercio_proveedores = fields.Many2one('comercio_proveedor', 'Tipo de comercio del proveedor', ondelete='cascade', select=True)
    servicio_proveedores = fields.Many2one('servicio_proveedor', 'Tipo de servicio del proveedor', ondelete='cascade', select=True)
    encargado_cobros = fields.Char('Encargado de cobros')
    empresa2 = fields.Many2one('res.partner', 'Empresa')
    empresados = fields.Many2one('empresa_2', 'Empresa', ondelete='cascade', select=True)
    i_pago = fields.Char('Instrucciones para pago')
    plazo_clientes = fields.Many2one('plazo_cliente', 'Plazo del pago de cliente', ondelete='cascade', select=True)
    plazo_proveedores = fields.Many2one('plazo_proveedor', 'Plazo del pago de cliente', ondelete='cascade', select=True)
    c_supervisor = fields.Many2one('res.partner', 'Supervisor')
    c_seguimiento = fields.Char('Nivel de seguimiento')
    c_encargado_pagos = fields.Char('Encargado de pagos')
    c_encargado_operaciones = fields.Char('Encargado de operaciones')
    c_gerente = fields.Char('Gerente')
    c_ultimo_seguimiento = fields.Date('Ultimo seguimiento')
    c_facebook = fields.Char('Facebook')
    c_twitter = fields.Char('Twitter')
    c_linkedin = fields.Char('Linkedin')
    c_direc_bodega = fields.Char('Direccion bodega')
    c_direc_fiscal = fields.Char('Direccion fiscal')
    c_direc_oficina = fields.Char('Direccion oficina')
    c_horario_recepcion = fields.Char('Horario de recepcion')
    c_horario_entrega = fields.Char('Horario de entrega')
    c_nombre = fields.Char('Nombre')
    c_seguimiento_prov = fields.Char('Nivel de seguimiento')
    # Pestaña conociendo a mi contacto
    c_nacimiento = fields.Date('Fecha de nacimiento')
    c_deporte_favorito = fields.Char('Deporte favorito')
    c_equipo_fut = fields.Selection([
                ('1', 'Barcelona'),
                ('2', 'Real Madrid')
            ])
    c_comida = fields.Char('Comida favorita')
    c_hobbies = fields.Text('Hobbies')
    c_name_hijo = fields.Char('Nombre hijo')
    c_cumple_hijo = fields.Date('Cumpleanios hijo')
    c_name_hijo2 = fields.Char('Nombre hijo')
    c_cumple_hijo2 = fields.Date('Cumpleanios hijo')
    c_restaurante = fields.Char('Restaurante favorito')


class tipo_base2(models.Model):
    _name = 'tipo_base2'
    _description = 'Proveedor'

    name = fields.Char('Descripcion', size=30)


class yservicio(models.Model):
    _name = 'yservicio'
    _description = 'Proveedor'

    name = fields.Char('Descripcion', size=30)


class ycomercio(models.Model):
    _name = 'ycomercio'
    _description = 'Proveedor'

    name = fields.Char('Descripcion', size=30)


class o_local(models.Model):
    _name = 'o_local'
    _description = 'Operador local'

    name = fields.Char('Descripcion', size=30)


class o_internacional(models.Model):
    _name = 'o_internacional'
    _description = 'Operador internacional'

    name = fields.Char('Descripcion', size=30)


class inactivo(models.Model):
    _name = 'inactivo'
    _description = 'Inactivo'

    name = fields.Char('Descripcion', size=30)


class tipo_base(models.Model):
    _name = 'tipo_base'
    _description = 'Tipo de base'

    name = fields.Char('Descripcion', size=30)


class busca_cliente(models.Model):
    _name = 'busca_cliente'
    _description = 'Que busca el cliente'

    name = fields.Char('Descripcion', size=30)


class estados_cliente(models.Model):
    _name = 'estados_cliente'
    _description = 'Estatus del Cliente'

    name = fields.Char('Descripcion', size=30)


class tipo_cliente(models.Model):
    _name = 'tipo_cliente'
    _description = 'Tipo Cliente'

    name = fields.Char('Descripcion', size=30)


class act_economica(models.Model):
    _name = 'act_economica'
    _description = 'Actividad economica'

    name = fields.Char('Descripcion', size=30)


class trafico_manejar(models.Model):
    _name = 'trafico_manejar'
    _description = 'Tipo de trafico a manejar'

    name = fields.Char('Descripcion', size=30)


class comercio_cliente(models.Model):
    _name = 'comercio_cliente'
    _description = 'Tipo de comercio del cliente'

    name = fields.Char('Descripcion', size=30)


class servicio_cliente(models.Model):
    _name = 'servicio_cliente'
    _description = 'Tipo de servicio del cliente'

    name = fields.Char('Descripcion', size=30)


class f_facturar(models.Model):
    _name = 'f_facturar'
    _description = 'Cuando se manda a facturar'

    name = fields.Char('Descripcion', size=30)


class f_internacional(models.Model):
    _name = 'f_internacional'
    _description = 'Tipo de factura servicio internacional'

    name = fields.Char('Descripcion', size=30)


class f_local(models.Model):
    _name = 'f_local'
    _description = 'Tipo de factura servicio local'

    name = fields.Char('Descripcion', size=30)


class r_factura(models.Model):
    _name = 'r_factura'
    _description = 'Dia de recepcion de factura'

    name = fields.Char('Descripcion', size=30)


class dia_pago(models.Model):
    _name = 'dia_pago'
    _description = 'Dia de pago'

    name = fields.Char('Descripcion', size=30)


class proveedor_para(models.Model):
    _name = 'proveedor_para'
    _description = 'Proveedor para'

    name = fields.Char('Descripcion', size=30)


class estatus_proveedor(models.Model):
    _name = 'estatus_proveedor'
    _description = 'Estatus de proveedor'

    name = fields.Char('Descripcion', size=30)


class act_proveedor(models.Model):
    _name = 'act_proveedor'
    _description = 'Actividad de proveedor'

    name = fields.Char('Descripcion', size=30)


class admon_proveedor(models.Model):
    _name = 'admon_proveedor'
    _description = 'Proveedor de administracion'

    name = fields.Char('Descripcion', size=30)


class oper_proveedor(models.Model):
    _name = 'oper_proveedor'
    _description = 'Proveedor de operaciones'

    name = fields.Char('Descripcion', size=30)


class comercio_proveedor(models.Model):
    _name = 'comercio_proveedor'
    _description = 'Tipo de comercio del proveedor'

    name = fields.Char('Descripcion', size=30)


class servicio_proveedor(models.Model):
    _name = 'servicio_proveedor'
    _description = 'Tipo de servicio del proveedor'

    name = fields.Char('Descripcion', size=30)


class plazo_cliente(models.Model):
    _name = 'plazo_cliente'
    _description = 'Plazo de pago de cliente'

    name = fields.Char('Descripcion', size=30)


class plazo_proveedor(models.Model):
    _name = 'plazo_proveedor'
    _description = 'Plazo de pago del proveedor'

    name = fields.Char('Descripcion', size=30)


class empresa_2(models.Model):
    _name = 'empresa_2'
    _description = 'Empresa'

    name = fields.Char('Descripcion', size=30)


