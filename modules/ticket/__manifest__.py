# -*- coding: utf-8 -*-
{
    'name': "My Tickets Module",
    'summary': "Custom module for tickets",

    'description': """
        This module is a custom module for tickets management, created for the purpose of learning Odoo development.
    """,

    'author': "NTSprint",
    'website': "https://www.ntsprint.com",

    'category': 'Uncategorized',
    'version': '18.0.0.0.1',

    'depends': ['base'],

    "data": [
        "security/ir.model.access.csv",
        "views/ticket_ticket_views.xml",
    ],
}

