# -*- coding: utf-8 -*-
# © 2017 Igor V. Kartashov
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": 'partner transport data',
    "version": "9.0.1.0",
    "summary": "specific data for transportation companies",
    "description": """
		i-vk
		v9.0.1.0
		specific data for transportation companies, applies to ASTIC and SETIR
	""",
    "author": "Igor V. Kartashov",
    "license": "AGPL-3",
    "website": "http://crm.setir.es",
    "category": "Partner",
    "depends": ['base'],
    "data": [
		"views/partnerTransport.xml",
		"data/data.xml",
    ],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}