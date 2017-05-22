# -*- coding: utf-8 -*-
# -*- transportJobPositions.py
from openerp import tools
from openerp import models, fields, api

class transportJobPositions ( models.Model):
	_name		= "transport.job.positions"
	_rec_name	= "x_strJobPosition" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario
	
	x_strJobPosition	= fields.Char ( string = "Cargo")