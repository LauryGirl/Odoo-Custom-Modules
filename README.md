[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/master/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/master/developer/howtos.html">the developer tutorials</a>


Odoo Project Setup
----
This repository contains the configuration for setting up an Odoo project. Follow the steps below to get your Odoo environment up and running.

Prerequisites

Python 3.6+
PostgreSQL
Node.js and npm

Setup Instructions
1. Clone the Repository
git clone <repository_url>
cd <repository_name>

2. Install Dependencies
Install the required Python packages.

pip install -r requirements.txt

3. Set Up PostgreSQL
Create a PostgreSQL database and user for Odoo.

CREATE DATABASE odoo;
CREATE USER odoo WITH ENCRYPTED PASSWORD 'odoo';
GRANT ALL PRIVILEGES ON DATABASE odoo TO odoo;

4. Configure Odoo
Edit the odoo.conf file to configure the database connection.

[options]
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
addons_path = addons,modules

5. Install Node.js Packages
Install the necessary Node.js packages.

npm install -g less less-plugin-clean-css

6. Install wkhtmltopdf
Download and install wkhtmltopdf from wkhtmltopdf.org.

7. Run Odoo
Start the Odoo server.

python odoo-bin -c odoo.conf

8. Access Odoo
Open your web browser and go to http://localhost:8069 to access the Odoo web interface.

9. Configure Odoo
Create a New Database: Follow the on-screen instructions to create a new database.
Install Modules: Navigate to the Apps menu and install the necessary modules for your project.
Customize Settings: Configure the settings according to your project requirements.

10. Develop Custom Modules
Create a Custom Module: Use the odoo-bin scaffold command to create a new module.

python odoo-bin scaffold <module_name> modules

Install the Module: Go to the Apps menu, update the app list, and install your custom module.

11. Update and Maintain
Update Modules: Use the Odoo web interface to update modules as needed.
Backup Database: Regularly backup your database to prevent data loss.
