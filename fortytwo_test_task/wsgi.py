"""
WSGI config for fortytwo_test_task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from fortytwo_test_task.settings import common
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortytwo_test_task.settings")

activate_env = os.path.expanduser(os.path.join(common.BASE_DIR, "ENV/bin/activate_this.py"))
execfile(activate_env, dict(__file__=activate_env))
# Django server
application = get_wsgi_application()

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
