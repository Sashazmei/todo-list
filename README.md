# 📋 To-Do List — Django Web Application

**To-Do List** is a web-based task management system built with Django and Django REST Framework.  
It allows users to register, create tasks, take responsibility for tasks, and manage them through both a modern web interface and a REST API.

---

## ✨ Features

- 🧑 User registration and login system
- 📝 Task creation and listing
- ✅ Marking tasks as taken (one user per task)
- 🔒 View which tasks are already in progress
- 🌐 RESTful API for external integrations
- 🖼 Clean, responsive UI with Bootstrap 5

---

## 🚀 Technologies Used

- **Python 3.12**
- **Django 5.2**
- **Django REST Framework**
- **Bootstrap 5** (for styling)
- **SQLite** (default database)

---

## ⚙️ Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://github.com/Sashazmei/todo-list.git
cd todo-list
python -m venv venv
# Activate the environment:
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
