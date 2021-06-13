from jqgrid.lib.base import BaseController
from jqgrid.model import DBSession, User
from tg import expose
from jqgrid.lib.jqgrid import jqgridDataGrabber
from tg import render_template

class DataBaseController(BaseController):

    def __init__(self):
        pass

    @expose('jqgrid.templates.loadingData.dataBase.index')
    def index(self, **kw):
        return dict(page='index')

    @expose('json')
    def loadGrid(self, **kw):
        filter = []
        return jqgridDataGrabber(User, 'user_id', filter, kw).loadGrid()

    @expose('json')
    def updateGrid(self, **kw):
        filter = []
        return jqgridDataGrabber(User, 'user_id', filter, kw).updateGrid()

    @expose('json')
    def open(self, **kw):
        if kw['user_id'] == "0":
            kw['user'] = User()
        else:
            kw['user'] = DBSession.query(User).filter_by(user_id=kw['user_id']).first()
        dialogtemplate = render_template(kw, "mako", 'jqgrid.templates.loadingData.form')
        return dict(dialogtemplate=dialogtemplate)

    @expose('json')
    def save(self,**kw):
        user = "ok"
        if kw['user_id'] == "0":
            new_user = User.add(kw['user_name'].lower(),kw['email_address'],kw['display_name'],kw['password'])
            return dict(error=new_user)
        else:
            if kw['action'] == "update":
                print("UPDATE")
                user = User.update(kw['user_id'],kw['user_name'].lower(),kw['email_address'],kw['display_name'],kw['password'])
            if kw['action'] == "delete":
                user = User.delete(kw['user_id'])
            return dict(error=user)