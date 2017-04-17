# -*- coding: utf-8 -*-
#-*- partnerTransportCountries.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransportCountries ( models.Model):
	_name = "partner.transport.countries"

	
	def get_countries ( self):
		l = []
		for r in self.env["res.country.group"].search ([('name','=', 'Europe')]).country_ids:
			l.append ((r.code, r.name))
		return l

	x_idPartner	= fields.Many2one ( "res.partner")
	x_eCountry	= fields.Selection ( string = "Country", selection = "get_countries")