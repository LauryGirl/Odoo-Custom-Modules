# -*- coding: utf-8 -*-

from odoo import models, fields, api
import mysql.connector


class Ticket(models.Model):
    _name = 'ticket.ticket'
    _description = 'My Tickets Module'
    _rec_name = "code" 

    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', default=fields.Date.today)

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