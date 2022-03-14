# -*- coding: utf-8 -*-
from odoo import models, fields

class horarios(models.Model):
    _name = "escolares.horarios"

    name = fields.Many2one('escolares.niveles', require='True', string='Niveles')
    horas = fields.Many2one('escolares.horas',string='Horas', require='True')
    carrera_id = fields.Many2one('escolares.carreras', string = 'Carrera')
    inscrito = fields.Many2one('escolares.alumnos', string = 'Inscrito')

