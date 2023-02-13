# Part-2

### Database Setup

We are using SQLite which is already included in python thus won't need
to anything else to support the database.

### 'migrate' Command
This command look at the **INSTALLED_APPS** setting and creates any necessary
database tables accoroding to the database setting in **mysite\setting.py**,
and database migrations shipped with the app.
```bash
$ python manage.py migrate
```
After this command you can run command-line client for sql as
```bash
sqlite3 db.sqlite3
.tables
```
This shows all the tables created by the migrate command

### Creating Models
To create models, create python class that subclasses **django.db.models.Model**
Each field is represented by instance of a Field class i.e CharField that tells
django what type of data each field holds.
Check polls/models.py

### Activating Models
Tell our project that polls app is installed by adding a reference to its
configuration class in the INSTALLED_APPS in mysite/setting.py, i.e PollsConfig class **polls/apps.py**

### makemigration command
By running makemigrations, you’re telling Django that you’ve made some changes to your models 
(in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
```bash
$ python manage.py makemigration polls
```
This create **polls/migrations/0001_initial.py** <br>
After creation of migrations, finally use migrate command to bring changes to the models
```bash
$ python manage.py migrate
```
The three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

### Python interractive shell
```bash
$ python manage.py shell
```

