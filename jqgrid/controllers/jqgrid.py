from jqgrid.lib.base import BaseController
from jqgrid.model import DBSession
from tg import expose
import requests
from base64 import b64decode
import datetime
import json
import base64
import os

class MyError(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class JqGridController(BaseController):

    def __init__(self):
        pass

    @expose('json')
    def open(self,**kw):
        print(kw)

    @expose('json')
    def load(self,**kw):
        print(kw)