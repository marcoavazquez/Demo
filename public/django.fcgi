#! / Usr / bin / python
import os, sys

_PROJECT_DIR = Os.path.dirname (os.path.dirname (os.path.abspath (FILE)))
sys.path.insert (0, _PROJECT_DIR)
sys.path.insert (0, os.path.dirname (_PROJECT_DIR))

_PROJECT_NAME _PROJECT_DIR.split = ('/') [-1]
os.environ ['DJANGO_SETTINGS_MODULE'] = "% s.settings"% _PROJECT_NAME

importación de django.core.servers.fastcgi runfastcgi
runfastcgi (method = "rosca", daemonize = "false")