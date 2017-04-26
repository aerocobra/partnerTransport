# -*- coding: utf-8 -*-
# -*- transportSectors.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportSectors ( models.Model):
	_name		= "transport.sectors"
	_rec_name	= "x_strSector" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	x_strSector	= fields.Char ( string = "Transport sector")