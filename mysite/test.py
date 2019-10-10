import os
import sys
#
## assuming your django settings file is at '/home/yununeAgashiNO1/mysite/mysite/settings.py'
## and your manage.py is is at '/home/yununeAgashiNO1/mysite/manage.py'
path = '/home/yununeAgashiNO1/anaconda_blog_test'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
#then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
