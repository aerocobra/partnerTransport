# -*- coding: utf-8 -*-
# -*- transportAssociations.py
from openerp import tools
from openerp import models, fields, api
from pygments.lexer import _inherit

class transportAssociations ( models.Model):
	_name = "transport.associations"

	x_strKey			= fields.Char ( string = "key")	
	x_strAssociation	= fields.Char ( string = "Transport association")