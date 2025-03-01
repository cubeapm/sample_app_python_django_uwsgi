# New Relic Instrumentation

This branch contains code for New Relic instrumentation.

CubeAPM works with New Relic agents as described in [using CubeAPM with New Relic agents](https://docs.cubeapm.com/instrumentation#using-cubeapm-with-new-relic-agents).

For testing, **ngrok** can be used in place of load balancer. Run `ngrok http 3130` to create a tunnel and use the domain name provided by ngrok to set `NEW_RELIC_HOST=xxxx.ngrok-free.app` in [docker-compose.yml](docker-compose.yml).

Refer the project README below for more details.

## Troubleshooting

If the app does not show up in CubeAPM after integration is done, add the below environment variables to check New Relic agent logs.

```shell
# Print New Relic agent logs on screen
NEW_RELIC_LOG=stdout

# Set New Relic agent log level to debug if needed to see detailed logs
#NEW_RELIC_LOG_LEVEL=debug
```

---

# Python Django uWSGI Instrumentation

This is a sample app to demonstrate how to instrument Python Django uWSGI app with **Datadog**, **Elastic**, **New Relic** and **OpenTelemetry**. It contains source code for the Django app which interacts with various services like Redis, MySQL, etc. to demonstrate tracing for these services. This repository has a docker compose file to set up all these services conveniently.

The code is organized into multiple branches. The main branch has the Django app without any instrumentation. Other branches then build upon the main branch to add specific instrumentations as below:

| Branch                                                                                         | Instrumentation | Code changes for instrumentation                                                                                |
| ---------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| [main](https://github.com/cubeapm/sample_app_python_django_uwsgi/tree/main)         | None            | -                                                                                                               |
| [datadog](https://github.com/cubeapm/sample_app_python_django_uwsgi/tree/datadog) | Datadog       | [main...datadog](https://github.com/cubeapm/sample_app_python_django_uwsgi/compare/main...datadog) |
| [elastic](https://github.com/cubeapm/sample_app_python_django_uwsgi/tree/elastic)         | Elastic   | [main...elastic](https://github.com/cubeapm/sample_app_python_django_uwsgi/compare/main...elastic)         |
| [newrelic](https://github.com/cubeapm/sample_app_python_django_uwsgi/tree/newrelic) | New Relic       | [main...newrelic](https://github.com/cubeapm/sample_app_python_django_uwsgi/compare/main...newrelic) |
| [otel](https://github.com/cubeapm/sample_app_python_django_uwsgi/tree/otel)         | OpenTelemetry   | [main...otel](https://github.com/cubeapm/sample_app_python_django_uwsgi/compare/main...otel)         |

# Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
docker compose up --build

# Run the following command in a separate terminal to apply the database migrations.
# This is only needed during first-time setup. Repeat executions are harmless though.
source ./bin/activate
python manage.py migrate
```

Django app will now be available at `http://localhost:8000/apis/`.

The app has various API endpoints to demonstrate integrations with Redis, MySQL, etc. Check out [apis/views.py](apis/views.py) for the list of API endpoints.

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
