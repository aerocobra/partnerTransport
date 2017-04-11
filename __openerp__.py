# -*- coding: utf-8 -*-
# © 2017 Igor V. Kartashov <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": 'partner transport data',
    "version": "9.0.1.0",
    "summary": "extended customer data",
    "description": """
		author: i-vk
		v9.0.1.0
		extended parner data, applies for ASTIC and SETIR
	""",
    "category": "Partner",
    "author": "Igor V. Kartashov",
    "website": "http://crm.setir.es",
    "license": "AGPL-3",
    "depends": ['base'],
    "data": [
		"views/partnerTransport.xml",
		"data/data.xml",
    ],
    "images": [
			"images/ivk.png",
			],
    "installable": True,
    "application": True,
	"auto_install": False,
    "price": 0.00,
    "currency": "EUR"
}