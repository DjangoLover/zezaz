#!/home/zezaz_dash/.pythonbrew/pythons/Python-2.7.5/bin python
import sys
import os

INTERP = "/home/zezaz_dash/.pythonbrew/pythons/Python-2.7.5/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd() + '/zezaz')
os.environ['DJANGO_SETTINGS_MODULE'] = "zezaz.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


