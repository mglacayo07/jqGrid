from jqgrid.lib.base import BaseController
from jqgrid.model import DBSession, User
from tg import expose
from jqgrid.lib.jqgrid import jqgridDataGrabber
import json

class UserController(BaseController):

    def __init__(self):
        pass

    @expose('jqgrid.templates.user.user_jqgrid')
    def index(self, **kw):
        return dict(page='type')

    @expose('json')
    def loadGrid(self, **kw):
        filter = []
        return jqgridDataGrabber(User, 'user_id', filter, kw).loadGrid()

    @expose('json')
    def updateGrid(self, **kw):
        filter = []
        return jqgridDataGrabber(User, 'user_id', filter, kw).updateGrid()