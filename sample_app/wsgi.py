"""
WSGI config for sample_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
# import logging

from django.core.wsgi import get_wsgi_application

# If using ELASTIC_APM_LOG_FILE to check agent debug logs, 
# The following may need to be uncommented to see the logs.

# logging.basicConfig()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_app.settings')

application = get_wsgi_application()
