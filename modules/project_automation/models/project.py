from odoo import api, fields, models
import mysql.connector
from mysql.connector import Error
import random

try:
    from . import config_db
except:
    # solve: create a file named config_db.py in the same directory as this file with the requirements
    config_db = None

class Project(models.Model):
    _inherit = 'project.project'

    def create_project_with_tasks(self):
        # Delete existing projects
        existing_projects = self.search([])
        for project in existing_projects:
            # Remove references in project_update
            self.env['project.update'].search([('project_id', '=', project.id)]).unlink()
            project.unlink()
        
        self.connect_with_mySQL()

    
    def connect_with_mySQL(self):
        """
        Connects to MySQL database and prints a message to the console
        """

        if not config_db:
            print("DATABASE_CONFIG is not defined. Please create config_db.py with the required database configuration.")
            return []
        
        try:
            connection = mysql.connector.connect(
                host = config_db.DATABASE_CONFIG['host'],
                user = config_db.DATABASE_CONFIG['user'],
                password = config_db.DATABASE_CONFIG['password'],
                database = config_db.DATABASE_CONFIG['database']
            )

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                query = """
                    SELECT 
                        tt.Name as teamName,
                        tt.Email as teamEmail,
                        tt.Ref as teamRef,
                        pct.taskStatusId,
                        pct.taskDailyStatusId,
                        pct.taskLink,
                        pct.taskDescription,
                        pct.taskTitle,
                        pct.taskPeriodDate,
                        pct.taskCreatedDate,
                        pct.taskOriginalEstimate,
                        pct.taskTotalWorkedTime,
                        pct.projectName,
                        pct.projectManagementPlatformUrl,
                        pct.projectDescription,
                        pct.projectStatus,
                        pct.projectLastComment,
                        pct.projectStartDate,
                        pct.projectEndDate,
                        pct.companyName,
                        pct.companyStatus,
                        pct.companyLogo,
                        pct.companyURL
                    FROM ntsprint.teams tt
                        inner join
                        (SELECT 
                            t.StatusId as taskStatusId,
                            t.DailyStatusId as taskDailyStatusId,
                            t.Link as taskLink,
                            t.Description as taskDescription,
                            t.Title as taskTitle,
                            t.Period as taskPeriodDate,
                            t.CreatedAt as taskCreatedDate,
                            t.OriginalEstimate as taskOriginalEstimate,
                            t.TotalWorkedTime as taskTotalWorkedTime,
                            pc.projectName,
                            pc.projectManagementPlatformUrl,
                            pc.projectDescription,
                            pc.projectStatus,
                            pc.projectLastComment,
                            pc.companyName,
                            pc.companyStatus,
                            pc.companyLogo,
                            pc.teamId,
                            pc.projectStartDate,
                            pc.projectEndDate,
                            pc.companyURL
                        FROM ntsprint.tasks t
                            inner join
                            (SELECT 
                                p.Id as projectId,
                                p.Name as projectName, 
                                p.ManagementPlatformUrl as projectManagementPlatformUrl, 
                                p.Description as projectDescription, 
                                p.Status as projectStatus, 
                                p.LastComment as projectLastComment, 
                                p.TeamId as teamId,
                                p.StartDate as projectStartDate,
                                p.EndDate as projectEndDate,
                                c.Name as companyName,
                                c.Status as companyStatus,
                                c.Logo as companyLogo,
                                c.URL as companyURL
                            FROM ntsprint.projects p 
                                inner join 
                                ntsprint.companies c on p.CompanyId = c.Id) pc
                            on pc.projectId = t.ProjectId) pct 
                        on tt.Id = pct.teamId
                    order by pct.projectStartDate desc        
                """

                cursor.execute(query)
                
                records = cursor.fetchall()

                for record in records:
                    self.create_project(record)


                cursor.close()
                connection.close()

                return records

            return []

        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return []
    
    def create_project(self, record):
        print(record)

        project_values = {
            'name': record['projectName'],
            'user_id': self.get_user_id(record),
            'date_start': record['projectStartDate'],
            'description': record['projectDescription'],
            'partner_id': self.get_partner_id(record),
            'last_update_color': self.get_random_color()
        }

        project = self.search([('name', '=', record['projectName'])], limit=1)
        if not project:
            project = self.create(project_values)

        self.create_task(record, project)


    def get_user_id(self, record):
        user_name = record['teamName']

        user = self.env['res.users'].search([('name', '=', user_name)], limit=1)
        if not user:
            user = self.env['res.users'].create({
                'name': user_name,
                'login': user_name.lower().replace(' ', '_'),
                'email': record['teamEmail'],       
            })
        return user.id
    
    def get_partner_id(self, record):
        partner_name = record['companyName']
        partner = self.env['res.partner'].search([('name', '=', partner_name)], limit=1)
        if not partner:
            partner = self.env['res.partner'].create({
                'name': partner_name,
                'company_type': 'company',
                'is_company': True,
                'website': record['companyURL'],
            })
        return partner.id
    
    def create_task(self, record, project):
        task_values = {
            'name': record['taskTitle'],
            'description': record['taskDescription'],
            'date_deadline': record['taskCreatedDate'],
            'user_id': self.env.user.id, #Assign to the current user (Temporal Solution)
            'project_id': project.id,
            'priority': '1', 
            'sequence': 10,  # Example value
            'color': self.get_random_color(), 
        }
        

        self.env['project.task'].create(task_values)
    
    def get_random_color(self):
        """
        Returns a random color (integer from 0 to 9) for a task
        """
        colors = list(range(9))  # Colors from 0 to 9
        return random.choice(colors) + 1
                
        
    

class Task(models.Model):
    _inherit = 'project.task'

    user_id = fields.Many2one('res.users', string='Assigned to')