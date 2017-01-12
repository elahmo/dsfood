#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/dsfood")

from app import app as application
application.secret_key = 'dsfood-comp6235-group2'
