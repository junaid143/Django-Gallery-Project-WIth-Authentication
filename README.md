To Run This Project 

Step 1 
create Virtual enviroment and activate 
Window 
>>>pip install virtualenv 

>>>virtualenv env
or
>>>python -m venv env

activate enviroment

>>>env\scripts\activate

Step 2
install project dependencies
>>>pip install django
>>>pip install pillow

Step 3
>>>python manage.py makemigrations

>>>python manage.py migrate

>>>python manage.py createsuperuser

Step 4

login to admin pannel 
http://127.0.0.1:8000/admin

and add categories 
eg
Mountains
Beaches
Nature
Sports
Super Heros

Step 5

Add images for thos Such Categories
