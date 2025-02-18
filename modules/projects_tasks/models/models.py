# -*- coding: utf-8 -*-

from odoo import models, fields, api
import mysql.connector


class projects(models.Model):
    _name = 'projects_tasks.projects'
    _description = 'projects_tasks.projects'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    def projects_mysql(self):
        try:
            # Configura la conexión a la base de datos MySQL
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="ntsprint"
            )

            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM projects LIMIT 10")
                records = cursor.fetchall()

                for record in records:
                    print(record)

                cursor.close()
                connection.close()

        except mysql.connector.Error as e:
            print(f"Error al conectarse a MySQL: {e}")

    @api.depends('value')
    def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100