# Primary Key
You don't need to specifically define a primary key in models because Django will by default create one for you.

# Database Synchronization
After you make some changes to the models, you want to synchronize the changes to the database. Run this command:
```
python manage.py makemigrations
```

so that Django can start to search for the changes. It will show you the results of its research. And if everything looks okay, you can run
```
python manage.py migrate
```
to actually synchronize with the database.

# Superuser
```
python manage.py createsuperuser
```

and then you can log in the admin interface with this user.

