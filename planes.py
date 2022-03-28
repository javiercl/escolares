# -*- coding: utf-8 -*-
from odoo import models,fields

class planes(models.Model):
    _name = 'escolares.planes'

    name = fields.Char(string='Plan')
    state = fields.Selection([('activo','Activo'),('terminado','Terminado')],string='Estado')
    niveles = fields.One2many('escolares.niveles', 'plan_id', string='Niveles')

    _sql_constraints = [
        ('unique_planes', 'unique(name)', 'El plan de estudios ya existe!')
    ]

class niveles(models.Model):
    _name = 'escolares.niveles'

    name = fields.Char(string='Nivel')
    plan_id = fields.Many2one('escolares.planes',string='Plan')
    modalidad = fields.Selection([('intensivo','Intensivo'),('normal','Normal'),('avanzado','Avanzado'),('sabatino','Sabatino')],string='Modalidad')

    _sql_constraints = [
        ('unique_niveles', 'unique(name)', 'El nivel ya esxiste para este plan!')
    ]