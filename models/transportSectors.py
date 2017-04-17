# -*- coding: utf-8 -*-
# -*- transportSectors.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportSectors ( models.Model):
	_name = "transport.sectors"

	x_strKey	= fields.Char ( string = "key")	
	x_strSector	= fields.Char ( string = "Transport sector")