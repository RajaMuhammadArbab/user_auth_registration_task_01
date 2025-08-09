# Django User Authentication System

## Tech Stack Used
- Python 3.12
- Django 5.2.4
- SQLite (default database)
- HTML, CSS (for frontend templates and styling)

---

## Setup & Run Instructions

### Prerequisites
- Python 3.12 installed on your system
- `pip` package manager available

### Steps

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd user_auth_registration
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the app in your browser:**

   - Registration page: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)
   - Login page: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
   - Dashboard page (after login): [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)

---

## Project Structure Overview

```
user_auth_registration/
├── accounts/             # Django app for authentication
├── templates/            # HTML templates (login, register, dashboard)
├── static/               # CSS, JS, and other static files
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database file
└── user_auth_registration/  # Project settings and URLs
```

---

## Notes

- Passwords are securely hashed by Django’s default authentication system.
- CSS styles are loaded from the `static/css/style.css` file.
- Make sure to create the `static` and `templates` directories with necessary files before running the app.

---


<img width="800" height="937" alt="1" src="https://github.com/user-attachments/assets/e6f3daee-8f95-4740-ac1f-505bec0871ef" />






