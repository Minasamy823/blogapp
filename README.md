# To run locally, do the usual:

    Create a Python 3.5 virtualenv

    Install dependencies:

    pip install -r requirements.txt

    #Configure the database:
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_apassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

     #Configure migrations

         python manage.py makemigrations
         python manage.py migrate

     #Initiate data

         python manage.py init-data

     #runserver on the localhost

         python manage.py runserver

