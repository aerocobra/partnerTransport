# -*- coding: utf-8 -*-
# -*- transportAuthorizations.py
from openerp import tools
from openerp import models, fields, api

class transportAuthorizations ( models.Model):
	_name = "transport.authorizations"
	_rec_name	= "x_strAuthorization" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	x_strAuthorization	= fields.Char ( string = "Autorización")