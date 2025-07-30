
#  Django User Authentication System

A simple Django web application that allows users to **Register**, **Login**, access a secure **Dashboard**, and **Logout**. Passwords are securely hashed, and user sessions are managed using Django’s built-in authentication framework.

---

##  Tech Stack

-  Python 3.x
-  Django 4.x
-  SQLite3 (default Django DB)
-  Django Auth System
-  HTML5/CSS3 (Templates)
-  Optional: bcrypt (for stronger password hashing)

-

##  Setup Instructions

### 1. Clone the repository or download ZIP
```bash
git clone https://github.com/your-username/user_registration.git
cd user_registration
```

### 2. Create and activate virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  

```

### 3. Install dependencies
```bash
pip install django
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  Features

-  User Registration with email & full name
-  Password confirmation & email uniqueness check
-  Login using email & password
-  Dashboard visible only to logged-in users
-  Logout support
-  Password hashing with Django’s secure system


