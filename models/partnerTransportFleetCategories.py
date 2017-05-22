# -*- coding: utf-8 -*-
#-*- partnerTransportFleetCategories.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportFleetCategories ( models.Model):
	_name		= "partner.transport.fleet_categories"
	_rec_name	= "x_eFleetCategory" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	def get_fleet_categories ( self):
		l = []
		for r in self.env["transport.fleet_categories"].search ([('id','>',-1)]):
			l.append ( ( "fc-" + str(r.id), r.x_strFleetCategory))
		return l

	x_idPartner			= fields.Many2one	(	comodel_name	= "res.partner")
	x_eFleetCategory	= fields.Selection	(
												string			= "Flota",
												selection		= "get_fleet_categories"
											)
	x_nFleetCategory	= fields.Integer	(	string			= "Cantidad")