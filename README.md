the folders present in the project are:
1 - cms (the main project folder)
2 - media (the folder to save the uploaded files)
3 - college (the application folder)
4 - users (the application folder for authentication)
5 - db.sqlite3 (db file)
6 - manage.py (django manage file to do operations)


instructions:-

1- install the libraries:
pip install django djangorestframework spacy
python -m spacy download en_core_web_sm
pip install django-cors-headers
pip install djangorestframework-simplejwt

2- install the django project:
django-admin startproject myproject || python -m django startproject myproject

cd myproject

3- migrating the project to setup the database:
python manage.py makemigrations
python manage.py migrate

4- install the application in the project:
python manage.py startapp myapp


 

