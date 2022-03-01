# -*- coding: utf-8 -*-
from odoo import models,fields

class carreras(models.Model):
    _name = 'escolares.carreras'

    name = fields.Char(string='Clave de la carrera x', size=10, required="True")
    nombre = fields.Char(string='Clave de la carrera', size=60, required="True")

    _sql_constraints = [
        ('unique_carreras', 'unique (name)', 'La carrera ya existe!')
    ]