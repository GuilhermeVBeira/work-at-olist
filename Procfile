release: python manage.py migrate
release: python manage.py loaddata fixture_tax.json
web: gunicorn callapi.wsgi --log-file -
