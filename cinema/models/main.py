# -*- coding: utf-8 -*-

from openerp import fields,models,api

class peliculas_cine(models.Model):
	_inherit="product.template"
	_name="peliculas"

	name=fields.Char(string="Título")
	state = fields.Selection([('en cartel', 'En cartel'),('proximamente', 'Próximamente'),('pasada', 'Pasada')], "Estado", select=True, required=True)
	estado= fields.Selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')], default='draft')
	
	def confirm(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'confirmed'},context=None)
		return True
	
	def cancel(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'cancel'},context=None)
		return True
		
	def draft(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'draft'},context=None)
		return True
	
peliculas_cine()

class socios_cine(models.Model):
	_inherit="res.partner"
	_name="res.partner"

	customer = fields.Boolean("Socio")
	id = fields.Integer("Número de socio")
	es_socio = fields.Boolean("Socio:")

socios_cine()

class empleados_cine(models.Model):
	_inherit="hr.employee"
	_name="hr.employee"
	
	fecha_contratado=fields.Date("Fecha de contratación:")
	responsable_sala = fields.Many2one("salas", "Salas", delegate=True)

empleados_cine()