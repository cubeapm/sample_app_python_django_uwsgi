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
from opentelemetry.sdk import resources
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.system_metrics import SystemMetricsInstrumentor
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.pymysql import PyMySQLInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from socket import gethostname

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
    resource = resources.Resource.create({
        resources.HOST_NAME: gethostname() or 'UNSET',
        resources.PROCESS_PID : os.getpid(),
    })

    if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':
        trace_processor = SimpleSpanProcessor(ConsoleSpanExporter())
    else:
        trace_processor = BatchSpanProcessor(OTLPSpanExporter())
    trace_provider = TracerProvider(
        resource=resource,
        active_span_processor=trace_processor
    )
    trace.set_tracer_provider(trace_provider)

    if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':
        metric_exporter = ConsoleMetricExporter()
    else:
        metric_exporter = OTLPMetricExporter()
    metric_reader = PeriodicExportingMetricReader(exporter=metric_exporter)
    meter_provider = MeterProvider(
        resource=resource,
        metric_readers=[metric_reader]
    )
    metrics.set_meter_provider(meter_provider)
    SystemMetricsInstrumentor().instrument()


application = get_wsgi_application()
