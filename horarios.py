# -*- coding: utf-8 -*-
from odoo import models, fields

class horarios(models.Model):
    _name = "escolares.horarios"

    name=fields.Char(string='Clave horario')

    periodo = fields.Many2one('escolares.periodos', requireT='True', string='Periodo')
    plan = fields.Many2one('escolares.planes', require='True', string='Plan de estudio')
    nivel = fields.Many2one('escolares.niveles', require='True', string='Niveles')
    profesor = fields.Many2one('escolares.profesores', require='True', string='Profesores')
    horario = fields.Char(string='Horario')

    
    _sql_constraints = [
        ('unique_horarios', 'unique (name)', 'El horario ya existe!')
    ]

