# -*- coding: utf-8 -*-
from odoo import models, fields

class niveles(models.Model):
    _name='escolares.horas'

    name=fields.Char(string = 'Horas')

    _sql_constraints = [
        ('unique_nivel', 'unique (name)', 'La hora ya existe!')
    ]