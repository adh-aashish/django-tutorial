# Part-1

After installation of Django, go to the directory where you want to create project
``` bash
django-admin startproject mysite
```
This inturn creates the following files and folders
![image](https://user-images.githubusercontent.com/64474508/218244603-b2e18eca-ee93-4a9e-9405-4f8900063be8.png)

Go to the outer mysite directory
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](visit http://127.0.0.1:8000/)

## Creating a poll App
Go to the directory containing manage.py
```bash
python manage.py startapp polls
```
![image](https://user-images.githubusercontent.com/64474508/218245274-24fa2b04-4456-44ea-9011-431876c8c5e3.png)
- create views in views.py
- to call that view, map to a url in urls.py of poll app
- point the root URLconf at the polls.urls module
- for that use include() method; Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
- path() method takes urls, view, kwargs, name
