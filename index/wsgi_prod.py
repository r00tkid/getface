"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os, sys

from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))

settings_module = "%s.settings_prod" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
os.environ.setdefault("DJANGO_SETTINGS_ENVIRONMENT", "prod")

get_face = get_wsgi_application()
