# 🍽️ Kitchen Project

Django project for managing a restaurant kitchen.

## 🔗 Check it out!

**Kitchen project deployed on Render:**  
https://restaurant-kitchen-service-0yy7.onrender.com/

**Demo Login:** `user`  
**Demo git statusPassword:** `user12345`

## ⚙️ Installation

Python 3 must be already installed.

```shell
git clone https://github.com/Yurii-Hvozd/restaurant-kitchen-service
cd restaurant-kitchen-service

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

## ✨ Features

- Authentication functionality for Cook/User
- Managing cooks, dishes, ingredients and dish types
- Assigning cooks and ingredients to dishes
- Search functionality
- Pagination
- Detailed dish information
- Admin panel for advanced management