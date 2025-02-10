"""
WSGI config for sample_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from uwsgidecorators import postfork
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.pymysql import PyMySQLInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_app.settings')

DjangoInstrumentor().instrument()
PyMySQLInstrumentor().instrument()
RedisInstrumentor().instrument()
RequestsInstrumentor().instrument()
# Additional instrumentation can be enabled by
# following the docs for respective instrumentations at
# https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation
@postfork
def init_tracing():
    provider = TracerProvider()
    if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':
        processor = SimpleSpanProcessor(ConsoleSpanExporter())
    else:
        processor = BatchSpanProcessor(OTLPSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)


application = get_wsgi_application()
