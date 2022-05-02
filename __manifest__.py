# -*- coding: utf-8 -*-
{
    'name': 'Escolares',
    'version': '1.0',
    'category': 'Universidades',
    'description': 'Control Escolar',
    'author': 'Javier Cisneros,Jorge Cerda,Enrique Huerta,Cesar Soria,Geronimo,Gasca Jesus, Miguel Valdovinos',
    'maintainer': 'ITSA',
    'website': 'http://www.itsa.edu.mx',
    'depends': ['base'],
    'data': [
        'security/grupos.xml',
        'security/ir.model.access.csv',
        'views/alumnos_view.xml',
        'views/carreras_view.xml',
        'views/periodos_view.xml',
        'views/profesores_view.xml',
        'views/planes_view.xml',
        'views/inscripciones_view.xml',
        'views/horarios_view.xml',
        'views/grupos_view.xml',
        'reports/kardex.xml',
        'views/menu_view.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}