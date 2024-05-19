# nl2query [postgres] - Ramailo

### Requirements
1. Make sure you have installed python3 [Recommended : Python 3.11.4]
2. Setup virtualenv
```
$ python3 -m venv venv
```
3. Activate virtualenv
```
source venv/bin/activate
```

### Run the app in terminal

1. Start a Postgres database server on your machine or in the cloud.
2. Set the values in env.uat as per .env.example file

```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```

3. Setup a password to login to the Django admin dashboard.

```
python manage.py createsuperuser 0.0.0.0:8000
```

4. Create a new app. Run following from root folder

```
python manage.py startapp [app_name]

```

### Make API calls against the server

1. Go to [http://localhost:8000/admin](http://localhost:8000/admin) and login to the dashboard using username `admin` and the password you chose in step 1 above.
