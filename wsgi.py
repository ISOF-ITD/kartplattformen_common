"""
WSGI config for ortnamnsregistret project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "sagendatabas.settings"

sys.path.append('/var/www/django/sagendatabas')
sys.path.append('/var/www/django/sagendatabase/sagendatabas')

application = get_wsgi_application()
