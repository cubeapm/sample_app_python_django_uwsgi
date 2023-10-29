# Python Django uWSGI OpenTelemetry Instrumentation

This is a sample app to demonstrate how to instrument Python Django uWSGI app with OpenTelemetry. It contains source code for the Django app which interacts with various services like Redis, MySQL, etc. to demonstrate tracing for these services. This repository has a docker compose file to set up all these services conveniently.

This repository is inentionally designed to work with any OpenTelemetry backend, not just CubeAPM. In fact, it can even work without any OpenTelemetry backend (by dumping traces to console, which is also the default behaviour).

## Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
docker compose up --build

# Run the following command in a separate terminal to apply the database migrations.
# This is only needed during first time setup. Repeat executions are harmless though.
python manage.py migrate
```

Django app will now be available at `http://localhost:8000/apis/`.

The app has various API endpoints to demonstrate OpenTelemetry integrations with Redis, MySQL, etc. Check out [apis/views.py](apis/views.py) for the list of API endpoints. Hitting an API endpoint will generate the corresponding traces. Traces are printed to console (where docker compose is running) by default. If you want to send traces to a backend tool, comment out the `OTEL_LOG_LEVEL` line and uncomment the `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` line in [docker-compose.yml](docker-compose.yml).

## Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
