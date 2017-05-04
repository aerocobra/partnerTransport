# -*- coding: utf-8 -*-
# -*- transportAssociations.py
from openerp import tools
from openerp import models, fields, api

class transportAssociations ( models.Model):
	_name		= "transport.associations"
	_rec_name	= "x_strAssociation" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario
	
	x_strAssociation	= fields.Char ( string = "Asociación")