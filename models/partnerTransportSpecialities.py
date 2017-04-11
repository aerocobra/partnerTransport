# -*- coding: utf-8 -*-
#-*- partnerTransportSpecialities.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportSpecialities ( models.Model):
	_name = "partner.transport.specialities"

	def get_specialities ( self):
		l = []
		for r in self.env["transport.specialities"].search ([('id','>',-1)]):
			l.append ( ( r.x_strKey, r.x_strSpeciality))
		return l

	x_idPartner		= fields.Many2one ( "res.partner")
	x_eSpeciality	= fields.Selection ( string = "Transport specilality", selection = "get_specialities")