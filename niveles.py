# -*- coding: utf-8 -*-
from odoo import models, fields

class niveles(models.Model):
    _name='escolares.niveles'

    name=fields.Char(string = 'Niveles')

    _sql_constraints = [
        ('unique_nivel', 'unique (name)', 'El nivel ya existe!')
    ]