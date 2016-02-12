# -*- coding: utf-8 -*-

from openerp import fields,models, api

class sesiones_cine(models.Model):
	_inherit="event.event"
	_name="sesiones"
	_rec_name="name"

	name=fields.Many2one('peliculas', 'Pelicula', domain=[("state", "=", "en cartel")], required=True)
	sala=fields.Many2one('salas', 'Sala', required=True)
	seats_max=fields.Integer('Capacidad', compute="_compute_seats")
	seats_available=fields.Integer('Quedan', compute="_compute_seats")
	#butacas=fields.Selection(selection='_choose_butacas')
	entradas=fields.One2many('entradas', inverse_name='event_id') 

	@api.depends('sala', 'entradas')
	def _compute_seats(self):
		self.seats_max=0
		for fila in self.sala.filas:
			self.seats_max=self.seats_max+fila.n_butacas
		self.seats_available=self.seats_max
		for entrada in self.entradas:
			self.seats_available = self.seats_available - entrada.nb_register

	## def name_get(self)
	
sesiones_cine()

class entradas_cine(models.Model):
	_inherit="event.registration"
	_name="entradas"

	partner_id = fields.Many2one('res.partner', 'Socio', domain=[("es_socio", "=", True)])
	precio = fields.Selection([(5, 'Reducida'),(7, 'Normal')], "Tarifa", readonly=True)
	total=fields.Float("Total", compute="_compute_total", readonly=True)
	nb_register=fields.Integer('Cantidad')
	event_id=fields.Many2one('sesiones', string="Sesión")

	
	@api.depends('partner_id','nb_register')
	def _compute_total(self):
		self.total = self.precio * self.nb_register

	@api.onchange('partner_id')
	def _precio_change(self):
		if self.partner_id.es_socio is True: 
			self.precio=5		
		else:
			self.precio=7	

entradas_cine()