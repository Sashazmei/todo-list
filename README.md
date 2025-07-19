# 📋 To-Do List — Django Web App

**To-Do List** — это веб-приложение для управления задачами, построенное на Django. Оно позволяет:

- 🧑 Регистрироваться и входить в систему
- 📝 Создавать задачи
- 👤 Брать задачи на выполнение (один пользователь на задачу)
- 🔒 Видеть задачи, находящиеся в процессе выполнения
- 🎯 Работать в безопасной и современной среде

---

## 🚀 Используемые технологии

- Python 3.12  
- Django 5.2  
- Django REST Framework  
- Bootstrap 5  
- SQLite (по умолчанию)

---

## ⚙️ Установка

```bash
git clone https://github.com/Sashazmei/todo-list.git
cd todo-list
python -m venv venv
venv\Scripts\activate  # для Windows
# или source venv/bin/activate для Linux/macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
