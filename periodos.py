# -*- coding: utf-8 -*-
from odoo import models,fields

class periodos(models.Model):
    _name = 'escolares.periodos'

    name = fields.Char(string='Clave')
    descripcion = fields.Char(string='Descripcion')
    


    _sql_constraints = [
        ('unique_periodos', 'unique (name)', 'El periodo ya existe!')
    ]

