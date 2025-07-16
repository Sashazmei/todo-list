📋 To-Do List — Django Web App
This project is a web-based task manager built with Django. It allows users to:

🧑 Register and log in

📝 Create tasks

👤 Take tasks for execution (only one user per task)

🔒 See which tasks are already in progress

🎯 Work in a secure and modern environment

🚀 Technologies Used
Python 3.12

Django 5.2

Bootstrap 5 (for styling)

SQLite (default database)

⚙️ Installation
bash
git clone https://github.com/Sashazmei/todo-list.git
cd todo-list
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🔐 Authentication
Register at /register

Log in at /accounts/login/

After login, you can create and take tasks

📂 Project Structure
tasks/ — main application logic for tasks

templates/ — Bootstrap-styled HTML templates

registration/ — login and registration pages

🧑‍💻 Author
github.com/Sashazmei


# Todo List

Application “Todo List” на Django — »
Allows you to create, edit and delete tasks (ToDo).
Implemented using Django + Django REST Framework.
Supports API for task management.
Quickly deployed with the command:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver