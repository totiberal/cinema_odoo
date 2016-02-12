# -*- coding: utf-8 -*-

{
    "name": "Cinema",
    "version": "1,0",
    "category": "Ocio",
    "depends": [
                'base', 'sale', 'event', 'hr'               
                ],
    "author": "Gonzalo Iglesias & Alberto Álvarez",
    "description": "Módulo para la gestión de un cine.",
    "init_xml": [],
	'summary': 'Con este pequeño módulo se pretende dar soporte para la gestión de cines en Odoo',
    "data": [             
             'views/admin_cine_view.xml',
             'views/taquilla_cine_view.xml'
             ],
    "demo_xml": [],
    "installable": True,
    "auto-install": True,
    "active": False
}
