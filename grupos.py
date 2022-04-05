# -*- coding: utf-8 -*-
from odoo import models,fields

class grupos(models.Model):
    _name = 'escolares.grupos'

    name = fields.Char(string='Clave')
    periodo = fields.Many2one('escolares.periodos', string='Periodo')
    plan = fields.Many2one('escolares.planes',string='Plan')
    nivel = fields.Many2one('escolares.niveles',string='Nivel')
    profesor = fields.Many2one('escolares.profesores',string='Profesor')
    state = fields.Selection([('abierto','Abierto'),('cerrado','cerrado')],string='Estado')
    califs = fields.One2many('escolares.calificaciones','grupo',string='Calificaciones')
    _sql_constraints = [
        ('unique_grupos', 'unique (name)', 'El grupo ya existe!')
    ]

class calificaciones(models.Model):
    _name = 'escolares.calificaciones'

    grupo = fields.Many2one('escolares.grupos', string='Grupo')
    alumno = fields.Many2one('escolares.alumnos', string='Alumno')
    calif = fields.Float(string='calificacion')

    _sql_constraints = [
        ('unique_calificaciones', 'unique (grupo,alumno)', 'El alumno ya existe para este grupo!')
    ]
