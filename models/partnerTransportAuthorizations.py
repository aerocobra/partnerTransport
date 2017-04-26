# -*- coding: utf-8 -*-
#-*- partnerTransportAuthorizations.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportAutorizations ( models.Model):
	_name		= "partner.transport.authorizations"
	_rec_name	= "x_eAuthorization" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	def get_authorizations ( self):
		l = []
		for r in self.env["transport.authorizations"].search ([('id','>',-1)]):
			l.append ( ( "at-" + str(r.id), r.x_strAuthorization))
		return l

	x_idPartner			= fields.Many2one	( "res.partner")
	x_eAuthorization	= fields.Selection	( string = "Transport authorization", selection = "get_authorizations")
	x_nAuthorization	= fields.Integer	( string = "Amount")