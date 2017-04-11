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
	x_nTrucks		= fields.Integer ( string = "Trucks")
	x_nTrailers		= fields.Integer ( string = "Trailers")
	x_nRigidTrucks	= fields.Integer ( string = "Rigid Trucks")
	x_nBuses		= fields.Integer ( string = "Buses")
	x_nContainers	= fields.Integer ( string = "Containers")
	
	x_idsSectors		= fields.One2many ( "partner.transport.sectors", "x_idPartner", string="Sectores")
	x_idsSpecialities	= fields.One2many ( 'partner.transport.specialities', 'x_idPartner', string="Especialidades")
	x_idsAuthorizations	= fields.One2many ( 'partner.transport.autorizations', 'x_idPartner', string="Autirizaciones")
	x_idsAssociations	= fields.One2many ( 'partner.transport.associations', 'x_idPartner', string="Asociaciones")