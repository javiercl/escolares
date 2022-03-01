# -*- coding: utf-8 -*-
from odoo import models,fields
'''Comentario del Migue jaja saludos'''
class alumnos(models.Model):
    _name = 'escolares.alumnos'

    name = fields.Char(string='NControl')
    nombre = fields.Char(string='Nombre')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    inscrito = fields.Boolean(string='Inscrito?')
    carrera_id = fields.Many2one('escolares.carreras',string="Carrera")

    _sql_constraints = [
        ('unique_alumno', 'unique (name)', 'El alumno ya existe!')
    ]

