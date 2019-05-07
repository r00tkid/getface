import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

get_face = get_wsgi_application()
