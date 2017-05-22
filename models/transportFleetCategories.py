# -*- coding: utf-8 -*-
# -*- transportFleetCategories.py
from openerp import tools
from openerp import models, fields, api

class transportFleetCategories ( models.Model):
	_name		= "transport.fleet_categories"
	_rec_name	= "x_strFleetCategory" #IMPORTANTE - por este campo se hace la selección poe defecto en el formulario

	x_strFleetCategory	= fields.Char ( string = "Flota")