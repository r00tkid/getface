import os
import sys
from configurations.wsgi import get_wsgi_application

#sys.path.append('/home/shaman/workspace/get-face')
#sys.path.append('/home/shaman/miniconda3/envs/get_face/lib')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
#from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

get_face = get_wsgi_application()
