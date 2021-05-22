# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1621705712.8842502
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['head', 'title', 'head_content', 'body_class', 'main_menu', 'body', 'content_wrapper', 'footer', 'bottom_scripts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n\n<html>\n<head>\n  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n\n\n\n  <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" />\n  <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer('" />\n\n  ')
        __M_writer('\n</head>\n\n')
        if tg.auth_stack_enabled:
            if h.whoami()=="":
                __M_writer('       <meta http-equiv="refresh" content="0; url=')
                __M_writer(escape(tg.url('/')))
                __M_writer('" />\n')
            else:
                __M_writer('        <body class="')
                __M_writer(escape(self.body_class()))
                __M_writer('">\n          ')
                __M_writer(escape(self.main_menu()))
                __M_writer('\n          ')
                __M_writer(escape(self.footer()))
                __M_writer('\n        <!-- Insert nice scrool -->\n          ')
                __M_writer(escape(self.bottom_scripts()))
                __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n  <!-- Navbar -->\n')
        __M_writer('\n  ')
        __M_writer('\n  ')
        __M_writer('\n\n  <!-- Footer -->\n  ')
        __M_writer('\n\n  <script src="http://code.jquery.com/jquery.js"></script>\n  <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer('"></script>\n')
        __M_writer('\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        h = context.get('h', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <nav class="navbar navbar-default">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">\n        <img src="')
        __M_writer(escape(tg.url('/img/yuimx_logo.gif')))
        __M_writer('" height="20" alt="TurboGears 2"/>\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer('\n      </a>\n    </div>\n\n    <div class="collapse navbar-collapse" id="navbar-content">\n      <ul class="nav navbar-nav">\n')
        if tg.auth_stack_enabled:
            __M_writer('                <li><a href="')
            __M_writer(escape(tg.url('/user')))
            __M_writer('">JqGrid User</a></li>\n')
        __M_writer('      </ul>\n')
        if tg.auth_stack_enabled:
            __M_writer('            <ul class="nav navbar-nav navbar-right">\n')
            if h.whoami()=="":
                __M_writer('                <li><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer('">Login</a></li>\n')
            else:
                __M_writer('                <li><a href="')
                __M_writer(escape(tg.url('/user')))
                __M_writer('">JqGrid User</a></li>\n                <li><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer('">Logout</a></li>\n                <li><a href="')
                __M_writer(escape(tg.url('/admin')))
                __M_writer('">Admin</a></li>\n')
            __M_writer('            </ul>\n')
        __M_writer('    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        str = context.get('str', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')

        flash=tg.flash_obj.render('flash', use_js=False)
            
        
        __M_writer('\n')
        if flash:
            __M_writer('        <script>\n            $.alert("')
            __M_writer(escape(str(tg.flash_obj.pop_payload()['message'])))
            __M_writer('", { autoclose: false,type: \'info\',title: false});\n        </script>\n')
        __M_writer('    ')
        __M_writer(escape(self.body()))
        __M_writer('\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n      <!-- INSERT FOOTER -->\n      <div class="text-right">\n          <div class="credits">\n              <p>Copyright &copy; Maria Lacayo ')
        __M_writer(escape(h.current_year()))
        __M_writer('&nbsp;</p>\n          </div>\n      </div>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n <script type="text/javascript">\n\n </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "26": 1, "27": 6, "28": 6, "29": 10, "30": 10, "31": 11, "32": 11, "33": 13, "34": 16, "35": 17, "36": 18, "37": 18, "38": 18, "39": 19, "40": 20, "41": 20, "42": 20, "43": 21, "44": 21, "45": 22, "46": 22, "47": 24, "48": 24, "49": 27, "50": 28, "51": 30, "52": 32, "53": 68, "54": 69, "55": 80, "56": 90, "57": 93, "58": 93, "59": 98, "65": 13, "74": 28, "78": 28, "84": 30, "93": 32, "102": 34, "110": 34, "111": 43, "112": 43, "113": 44, "114": 44, "115": 45, "116": 45, "117": 51, "118": 52, "119": 52, "120": 52, "121": 54, "122": 55, "123": 56, "124": 57, "125": 58, "126": 58, "127": 58, "128": 59, "129": 60, "130": 60, "131": 60, "132": 61, "133": 61, "134": 62, "135": 62, "136": 64, "137": 66, "143": 69, "152": 70, "159": 70, "160": 71, "161": 72, "162": 73, "163": 74, "164": 73, "165": 74, "166": 75, "167": 76, "168": 76, "169": 79, "170": 79, "171": 79, "177": 83, "182": 83, "183": 87, "184": 87, "190": 94, "194": 94, "200": 194}}
__M_END_METADATA
"""
