```
poetry run shell
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py loaddata fixtures.json
python manage.py createsuperuser

python manage.py runserver localhost:8000
```

Visit:

http://localhost:8000/courses/

http://localhost:8000/courses/api/

http://localhost:8000/courses/modules/

http://localhost:8000/courses/modules/api/
