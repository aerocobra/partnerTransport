# -*- coding: utf-8 -*-
# -*- transportSpecialities.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportSpecialities ( models.Model):
	_name		= "transport.specialities"
	_rec_name	= "x_strSpeciality" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	x_strSpeciality	= fields.Char ( string = "Transport speciality")