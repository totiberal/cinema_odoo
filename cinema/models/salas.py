# -*- coding: utf-8 -*-

from openerp import fields,models,api

class salas_cine(models.Model):
	_name='salas'
	
	nombre=fields.Char('Nombre de sala:')
	capacidad=fields.Integer('Capacidad de sala:', compute="_compute_capacidad", readonly=True)
	tresd=fields.Boolean('3D:')
	descripcion_sala=fields.Text('Descripcion sala:')
	filas=fields.Many2many('fila_salas','n_butacas')

	state= fields.Selection([('draft','Borrador'),('confirmed','Confirmado'),('cancel','Cancelado')], default='draft')
	
	def confirm(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'confirmed'},context=None)
		return True
		
	##def confirm(self,cr,uid,ids,context=None):
		##self.write(cr,uid,ids,{'state':'confirmed'},context=None)
		##salas_obj=self.pool.get('salas')
		##salas_ids=salas_obj.search(cr, uid,[('state','=','confirmed')])
		
		##return {
			##'domain':"[('id','in',["+','.join(map(str,salas_ids))+"])]",
			##'name': 'Salas confirmadas',
			##'view_type': 'form',
			##'view_mode': 'tree,form',
			##'res_model': 'salas',
			##'view_id': False,
			##'type':'ir.actions.act_window',
		##}
	
	def cancel(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'cancel'},context=None)
		return True
		
	def draft(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'draft'},context=None)
		return True
	
	@api.depends('filas')
	def _compute_capacidad(self):
		self.capacidad=0
		for fila in self.filas:
			self.capacidad=self.capacidad + fila.n_butacas
	
salas_cine()

class fila_salas_cine(models.Model):
	_name="fila_salas"

	n_butacas=fields.Integer('Número de butacas')

fila_salas_cine()