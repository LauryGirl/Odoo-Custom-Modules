# -*- coding: utf-8 -*-
from urllib import request
from odoo import http


class ProjectsTasks(http.Controller):
    @http.route('/projects_tasks', type='http', auth='public')
    def connect_to_mysql(self):
        projects = request.env['projects_tasks.projects']
        projects.projects_mysql()
        return "Conexión a MySQL realizada. Revisa los logs para ver los resultados."
