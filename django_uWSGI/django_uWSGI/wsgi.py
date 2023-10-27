"""
WSGI config for django_uWSGI project.

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
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uWSGI.settings')

DjangoInstrumentor().instrument()

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
