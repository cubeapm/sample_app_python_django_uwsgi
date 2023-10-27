# sample_app_python_django_uWSGI
For Running this django_uWSGI app:-
OTEL_LOG_LEVEL=debug uwsgi --http :8000 --wsgi-file pages/tests.py

This app will now be available at http://localhost:8000/
