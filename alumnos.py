# -*- coding: utf-8 -*-
from odoo import models,fields, api

class alumnos(models.Model):
    _name = 'escolares.alumnos'

    name = fields.Char(string='NumControl')
    nombre = fields.Char(string='Nombre y Apellidos')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    inscrito = fields.Boolean(string='Inscrito?')
    carrera_id = fields.Many2one('escolares.carreras',string="Carrera")
    califs_ids = fields.One2many('escolares.calificaciones','alumno',string="Calificaciones")
    promedio = fields.Float(compute='calcular_promedio', string='Promedio')


    _sql_constraints = [
        ('unique_alumno', 'unique (name)', 'El alumno ya existe!')
    ]

    @api.depends('califs_ids')
    def calcular_promedio(self):
        prom = 0
        for c in self.califs_ids:
            prom = prom + c.calif
        if len(self.califs_ids) != 0:
            self.promedio = prom / len(self.califs_ids)
        else:
            self.prom = 0