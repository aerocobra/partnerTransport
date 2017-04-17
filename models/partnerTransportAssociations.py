# -*- coding: utf-8 -*-
#-*- partnerTransportAssociations.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportAssociations ( models.Model):
	_name = "partner.transport.associations"

	def get_associations ( self):
		l = []
		for r in self.env["transport.associations"].search ([('id','>',-1)]):
			l.append ( ( r.x_strKey, r.x_strAssociation))
		return l

	x_idPartner		= fields.Many2one ( "res.partner")
	x_eAssociation	= fields.Selection ( string = "Transport association", selection = "get_associations")
