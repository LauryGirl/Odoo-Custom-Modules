# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectsTasks(http.Controller):
#     @http.route('/projects_tasks/projects_tasks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projects_tasks/projects_tasks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projects_tasks.listing', {
#             'root': '/projects_tasks/projects_tasks',
#             'objects': http.request.env['projects_tasks.projects_tasks'].search([]),
#         })

#     @http.route('/projects_tasks/projects_tasks/objects/<model("projects_tasks.projects_tasks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projects_tasks.object', {
#             'object': obj
#         })

