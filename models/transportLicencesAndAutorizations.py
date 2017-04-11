# -*- transportAutorizations.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportAutorizations ( models.Model):
	_name = "transport.autorizations"

	x_strKey			= fields.Char ( string = "key")	
	x_strAuthorization	= fields.Char ( string = "Transport Autorization")