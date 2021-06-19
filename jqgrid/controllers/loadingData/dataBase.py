from jqgrid.lib.base import BaseController
from jqgrid.model import DBSession, User
from tg import expose
from jqgrid.lib.jqgrid import jqgridDataGrabber
from tg import render_template

class DataBaseController(BaseController):

    def __init__(self):
        pass

    @expose('jqgrid.templates.jqgrid.index')
    def index(self, **kw):
        colModel = self.colModel(**kw)
        params = dict(
            page = 'index',
            id = "dataBase",
            multi = "false",
            key = "user_id",
            sortorder = "asc",
            colModel = colModel
        )
        return params

    @expose('json')
    def colModel(self,**kw):
        colModel = [
            {"label": "User Name","index":"user_name","align":"left","hidden":"false","editable":"true","edittype":"text","search":"true"},
            {"label": "Email Adress", "index": "email_address","align":"left","hidden":"false","editable":"true","edittype":"text","search":"true"},
            {"label": "Display Name", "index": "display_name","align":"left","hidden":"false","editable":"true","edittype":"text","search":"true"},
            {"label": "Password", "index": "display_name", "align": "left", "hidden": "true", "editable": "true","edittype": "text", "search": "true"},
            {"label": "Created", "index": "created","align":"center","hidden":"false","editable":"true","edittype":"text","search":"true"}
        ]
        return colModel

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
        kw['id'] = "dataBase"
        if kw['user_id'] == "0":
            kw['user'] = User()
        else:
            kw['user'] = DBSession.query(User).filter_by(user_id=kw['user_id']).first()
        dialogtemplate = render_template(kw, "mako", 'jqgrid.templates.jqgrid.user_form')
        return dict(dialogtemplate=dialogtemplate)

    @expose('json')
    def save(self,**kw):
        user = "ok"
        id = "_dataBase"
        if kw['user_id'+id] == "0":
            new_user = User.add(kw['user_name'+id].lower(),kw['email_address'+id],kw['display_name'+id],kw['password'+id])
            return dict(error=new_user)
        else:
            if kw['action'] == "update":
                user = User.update(kw['user_id'+id],kw['user_name'+id].lower(),kw['email_address'+id],kw['display_name'+id],kw['password'+id])
            if kw['action'] == "delete":
                user = User.delete(kw['user_id'+id])
            return dict(error=user)