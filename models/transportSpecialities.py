# -*- transportSpecialities.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportSpecialities ( models.Model):
	_name = "transport.specialities"

	x_strKey		= fields.Char ( string = "key")	
	x_strSpeciality	= fields.Char ( string = "Transport speciality")