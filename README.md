# Message board app to display a simple message using class-based-views
## Commands
- pip install pipenv
- pipenv install django
- pipenv shell(activate virtual environment)
- django-admin startproject django_project . (create it in current directory)\\
- python manage.py startapp posts
- code .
- pip install python-dotenv(to keep the secret key)
- python manage.py migrate
- python manage.py runserver
- python manage.py createsuperuser

### Steps:
- Register app in settings.py
- create a post model
- Run migrations
- Create a superuser
- Register Post model to admin.py
- Add a posts in localhost/admin
- Create a base template directoey
- Register it in sttings.py
- Create a base.html 
- Create a home.html that inherits from base.html
- Display a simple message from the database