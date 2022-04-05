# -*- coding: utf-8 -*-
from odoo import models,fields,api

class inscripciones(models.Model):
    _name = 'escolares.inscripciones'

    peri = fields.Many2one('escolares.periodos', string='Periodo')
    alumno = fields.Many2one('escolares.alumnos',string='Alumno')
    plan = fields.Many2one('escolares.planes',string='Plan')
    nivel = fields.Many2one('escolares.niveles',string='Nivel')
    profesor = fields.Many2one('escolares.profesores',string='Profesor')
    horario = fields.Many2one('escolares.horarios',string='Horario')


    _sql_constraints = [
        ('unique_inscripciones', 'unique(peri,alumno)', 'El registro ya existe para este periodo!')
    ]
    
    @api.model
    def create(self,vals):
        # no existe
        grupo = self.env['escolares.grupos'].search([('periodo','=',vals['peri']),('plan','=',vals['plan']),('nivel','=',vals['nivel']),('profesor','=',vals['profesor'])])
        if grupo:
            valsx = {}
            valsx['grupo'] = grupo.id
            valsx['alumno'] = vals['alumno']
            valsx['calif'] = 0
            self.env['escolares.calificaciones'].create(valsx)
        else:
            valsx = {}
            valsx['periodo'] = vals['peri']
            valsx['plan'] = vals['plan']
            valsx['nivel'] = vals['nivel']
            valsx['profesor'] = vals['profesor']
            valsx['state'] = 'abierto'
            grp = self.env['escolares.grupos'].create(valsx)
            if grp:
                valsx = {}
                valsx['grupo'] = grp.id
                valsx['alumno'] = vals['alumno']
                valsx['calif'] = 0
                self.env['escolares.calificaciones'].create(valsx)

        return super(inscripciones,self).create(vals)

        #si existe, crear el alumno en calificaciones
        #si no existe, se crea el grupo y un alumno en calificacioes