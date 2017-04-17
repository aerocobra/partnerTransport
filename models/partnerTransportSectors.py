# -*- coding: utf-8 -*-
# -*- partnerTransportSectors.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportSectors ( models.Model):
	_name = "partner.transport.sectors"
	
	def get_sectors ( self):
		l = []
		for r in self.env["transport.sectors"].search ([('id','>',-1)]):
			l.append ( ( r.x_strKey, r.x_strSector))
		return l
	
	x_idPartner	= fields.Many2one	( "res.partner")
	x_eSector	= fields.Selection	( string = "Transport sector", selection = "get_sectors")