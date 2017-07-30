#!/usr/bin/env python
#coding:utf-8

import os
import sys

# 将系统的编码设置为UTF8
reload(sys)
sys.setdefaultencoding('utf8')
from django.core.wsgi import get_wsgi_application

path = '/usr/local/webserver/nginx/conf/django_project'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
application = get_wsgi_application()