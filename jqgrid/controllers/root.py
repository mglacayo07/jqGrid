# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
from jqgrid import model
from jqgrid.controllers.secure import SecureController
from jqgrid.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from jqgrid.lib.base import BaseController
from jqgrid.controllers.error import ErrorController

from jqgrid.controllers.loadingData.dataBase import DataBaseController
from jqgrid.controllers.loadingData.jsonData import jsonDataController
__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the jqGrid application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    dataBase = DataBaseController()
    jsonData = jsonDataController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "jqgrid"

    @expose('jqgrid.templates.index')
    def index(self):
        """Handle the front-page."""
        print("INDEX")
        return dict(page='index')

    @expose('jqgrid.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the loadingData login."""
        if failure is not None:
            if failure == 'loadingData-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the loadingData to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the loadingData to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)
