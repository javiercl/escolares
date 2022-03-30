# -*- coding: utf-8 -*-
from odoo import models,fields

class inscripciones(models.Model):
    _name = 'escolares.inscripciones'

    periodo = fields.Many2one('escolares.periodos', string='Periodo')
    alumno = fields.Many2one('escolares.alumnos',string='Alumno')
    plan = fields.Many2one('escolares.planes',string='Plan')
    nivel = fields.Many2one('escolares.niveles',string='Nivel')
    profesor = fields.Many2one('escolares.profesores',string='Profesor')
    horario = fields.Many2one('escolares.horarios',string='Profesor')


    _sql_constraints = [
        ('unique_inscripciones', 'unique(periodo,alumno)', 'El registro ya existe para este periodo!')
    ]