"""
WSGI config for navserver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from gps.gpsHandler import *
import subprocess

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'navserver.settings')

application = get_wsgi_application()



