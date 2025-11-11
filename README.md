Micro Project – Fullstack (Team 7)

Project Title: Pet Adoption Portal

Overview:
The Pet Adoption Portal is a Django-based web application designed to support responsible pet adoption and rehoming. The platform allows individuals to browse pets available for adoption, learn about each pet in detail, and obtain contact information to proceed with adoption. The system also includes a dedicated login for pet owners who wish to responsibly rehome their pets by uploading their pet's details to the portal. The project focuses on making the adoption process transparent and informative while promoting ethical treatment and care of pets.

Team Members:

Amulya B K (USN: 4MC23IS004)
Ananya A V (USN: 4MC23IS005)
Chinmayee M S (USN: 4MC23IS025)
Bhoomika B K (USN: 4MC23IS129)

Purpose of the Project:
The purpose of this system is to create an accessible and informative platform for people who want to adopt pets and for those who are looking to responsibly rehome their pets. By presenting clear adoption steps, pet details, and care guidance, the platform encourages informed decision-making and promotes responsible ownership.

Key Functionalities:
User Login and Signup System.
Separate login for individuals who want to rehome their pets.
Ability for registered pet owners to upload pet listings including name, breed, age, description, and images.
Browsing and viewing of available pets along with contact details of the person responsible for adoption.
Contact request functionality for adopters to send inquiries.
Admin panel access for backend management.
Organized templates, static content, and media handling.

User Workflow:
Step 1: User signs up or logs into the system.
Step 2: The user browses available pets.
Step 3: The user selects a pet to view complete details.
Step 4: The user gets clear information regarding where, how, and when the pet can be adopted, including owner contact details.
For individuals wishing to rehome a pet, a separate login is available where the owner can upload the pet profile and necessary information.

Project Structure (Important Directories):
pet_adoption/ (Main project folder with settings and URLs)
pets/ (Application containing models, views, templates, static files)
media/pet_images/ (Uploaded pet images are stored here)
templates/pets/ (HTML templates for all pages)
static/css/ (Stylesheets)
manage.py (Django project management script)

Technologies Used:
Python and Django Framework
HTML and CSS (Frontend structure and styling)
SQLite Database (Default Django storage)
Git and GitHub for version control

Steps to Run the Project:

Extract the project folder.
Open a terminal in the project directory.
Create a virtual environment (recommended):
python -m venv env
Activate on Windows: env\Scripts\activate
Activate on Mac/Linux: source env/bin/activate

Install required packages:
pip install django
pip install pillow

Apply migrations:
python manage.py migrate

Create a superuser (administrator):
python manage.py createsuperuser
Follow the prompts to set username and password.

Run the development server:
python manage.py runserver

Open the application in a browser:
http://127.0.0.1:8000

To access the admin panel:
http://127.0.0.1:8000/admin

Login using the superuser credentials you created.

Future Enhancements:
Integration of location-based pet matching.
Advanced filtering and search options.
SMS or email notification system for contact requests.
Mobile responsive UI improvements.
Multi-role permissions and dashboard analytics.

Conclusion:
This project provides a complete foundation for a digital pet adoption and rehoming system. It enables responsible adoption decisions, ensures proper information exchange, and encourages compassionate pet care. With further backend enhancements and feature expansion, this system can be scaled into a full adoption management platform.
