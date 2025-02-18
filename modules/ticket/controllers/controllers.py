# -*- coding: utf-8 -*-
# from odoo import http


# class Ticket(http.Controller):
#     @http.route('/ticket/ticket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ticket/ticket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ticket.listing', {
#             'root': '/ticket/ticket',
#             'objects': http.request.env['ticket.ticket'].search([]),
#         })

#     @http.route('/ticket/ticket/objects/<model("ticket.ticket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ticket.object', {
#             'object': obj
#         })

