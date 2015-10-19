=====
Django Secret Key
=====

Secret Key is a simple Django app to manage the SECRET_KEY variable.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Set your SECRET_KEY variable like this::

   from django_secret_key import DjangoSecretKey

   SECRET_FILE = os.path.join(BASE_DIR, 'projectname', 'secret.txt')
   SECRET_KEY = DjangoSecretKey(SECRET_FILE)
