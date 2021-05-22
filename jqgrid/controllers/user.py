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
        for x, y in kw.items():
            print("{} {}".format(x, y))
        page = kw["page"]
        records = []
        print(page)
        if page == "1":
            totalPages = 2
            selectedpage = 1

            id = "1"
            icc = "2345897458759"
            lifecyclestatus = "life1"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            id = "2"
            icc = "3452345235545"
            lifecyclestatus = "life2"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
            id = "3"
            icc = "323232323233223"
            lifecyclestatus = "life3"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
            id = "4"
            icc = "2345897458759"
            lifecyclestatus = "life1"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            id = "5"
            icc = "3452345235545"
            lifecyclestatus = "life2"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
        if page == "2":
            totalPages = 2
            selectedpage = 2
            id = "6"
            icc = "323232323233223"
            lifecyclestatus = "life3"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
        totalRecords = len(records)
        return dict(total=totalPages, page=selectedpage, records=totalRecords, rows=records)

    @expose('json')
    def updateGrid(self, **kw):
        filter = []
        return jqgridDataGrabber(User, 'user_id', filter, kw).updateGrid()