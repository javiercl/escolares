# -*- coding: utf-8 -*-
from odoo import models,fields

class profesores(models.Model):
    _name = 'escolares.profesores'

    name = fields.Char(string='Clave')
    nombre = fields.Char(string='Nombre y Apellido')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')


    _sql_constraints = [
        ('unique_profesores', 'unique (name)', 'El profesor ya existe!')
    ]

