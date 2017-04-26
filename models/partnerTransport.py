# -*- coding: utf-8 -*-
# -*- partnerTransport.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class partnerTransport ( models.Model):
	_inherit = "res.partner"

	x_eJobPosition	= fields.Selection (	string = "Cargo",
											selection = [	('director_general', 'Director General'),
															('director_financiero', 'Director Financiero'),
															('director_flota', 'Director Flota'),
															('sercretario', 'Secretario')])

#	x_nTrucks		= fields.Integer ( string = "Trucks")
#	x_nTrailers		= fields.Integer ( string = "Trailers")
#	x_nRigidTrucks	= fields.Integer ( string = "Rigid Trucks")
#	x_nBuses		= fields.Integer ( string = "Buses")
#	x_nContainers	= fields.Integer ( string = "Containers")

	x_idsFleet			= fields.One2many (
												comodel_name	= "partner.transport.fleet_categories",
												inverse_name	= "x_idPartner",
												string			= "Fleet")
	
	x_idsSectors		= fields.Many2many (
												comodel_name	= "transport.sectors",
												relation		= "rel_partner_sectors",
												column1			= "partner_id",
												column2			= "sector_id",
												string			= "Sectors"
											)

	x_idsSpecialities	= fields.Many2many (
												comodel_name	= "transport.specialities",
												relation		= "rel_partner_specialities",
												column1			= "partner_id",
												column2			= "speciality_id",
												string			= "Specialities"
											)

	x_idsAuthorizations	= fields.One2many (
												comodel_name	= "partner.transport.authorizations",
												inverse_name	= "x_idPartner",
												string			= "Autorizaciones")

	x_idsCountries		= fields.Many2many	(
												comodel_name	= "res.country",
												relation		= "rel_partner_countries",
												column1			= "partner_id",
												column2			= "country_id",
												string			= "Paises"
											)
	
	x_idsAssociations	= fields.Many2many	(
												comodel_name	= "transport.associations",
												relation		= "rel_partner_associations",
												column1			= "partner_id",
												column2			= "association_id",
												string			= "Associations"
											)
	@api.model
	def get_europe ( self):
		l = []
		for r in self.env["res.country.group"].search ([('name','=', 'Europe')]).country_ids:
			l.append ((r.id))
		return [('id', 'in', l)]