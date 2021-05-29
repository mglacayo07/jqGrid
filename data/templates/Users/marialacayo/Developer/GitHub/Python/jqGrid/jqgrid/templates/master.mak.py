# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1622253066.019812
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['meta', 'title', 'head_content', 'body_class', 'main_menu', 'content_wrapper', 'footer', 'bottom_scripts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery-1.11.0.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/bootstrap.min.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/grid.locale-es.js')))
        __M_writer('"></script>\n    <!-- This is the Javascript file of jqGrid -->\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery.jqgrid.src.js')))
        __M_writer('"></script>\n    <script type="text/ecmascript" src="')
        __M_writer(escape(tg.url('/lib/js/jquery-ui.min.js')))
        __M_writer('"></script>\n    <!-- This is the localization file of the grid controlling messages, labels, etc.\n    A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/lib/css/jquery-ui.css')))
        __M_writer('" />\n    <!-- The link to the CSS that the grid needs -->\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/lib/css/ui.jqgrid.css')))
        __M_writer('"  />\n    <link href="')
        __M_writer(escape(tg.url('/lib/fonts/font-awesome.min.css')))
        __M_writer('" rel="stylesheet" />\n    <meta charset="utf-8" />\n    <title>jqGrid</title>\n\n    <link href="')
        __M_writer(escape(tg.url('/lib/css/bootstrap.min.css')))
        __M_writer('" rel="stylesheet">\n    <script src="')
        __M_writer(escape(tg.url('/lib/stomp/stomp.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/moment/moment.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/js/alert.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/justgage/raphael-2.1.4.min.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/justgage/justgage.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/jqueryrotate/jQueryRotate.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')))
        __M_writer('"></script>\n    <script src="')
        __M_writer(escape(tg.url('/lib/timepicker/jquery-ui-timepicker-addon.js')))
        __M_writer('"></script>\n\n    <style type="text/css">\n        .dropdown {\n          background: rgba(255, 255, 255, 0.1);\n          float: left;\n          margin: 10px 8px;\n          padding: 0px;\n          border-radius: 4px;\n          list-style-type: none;}\n        .dropdown a.dropdown-toggle {\n          height: 40px;\n          width: 40px;\n          padding-top: 11px;\n          padding-left: 9px; }\n        .dropdown:hover {\n          color: #fff;\n          background: rgba(255, 255, 255, 0.2); }\n        .dropdown .label {\n          top: -4px;\n          left: 22px;\n          padding-top: 4px;\n          padding-bottom: 4px;\n          position: absolute;\n          border-radius: 9999px; }\n        .profile-sidebar {\n          padding: 10px 0;\n          border-bottom: 1px solid #e9ecf2; }\n        .label-success {\n          background-color: #8ad919; }\n        .label-danger {\n          background-color: #f9243f; }\n        .profile-userpic img {\n          float: left;\n          margin: 10px 0px 0px 15px;\n          width: 50px;\n          height: 50px;\n          border-radius: 9999px !important; }\n        .profile-usertitle {\n          float: left;\n          text-align: left;\n          margin: 10px 0 0 12px; }\n        .profile-usertitle-name {\n          font-size: 15px;\n          margin-bottom: 0px; }\n        .profile-usertitle-status {\n          text-transform: uppercase;\n          color: #AAA;\n          font-size: 10px;\n          font-weight: 600;\n          margin-bottom: 15px; }\n        .indicator {\n          width: 10px;\n          height: 10px;\n          display: inline-block;\n          border-radius: 9999px;\n          margin-right: 5px; }\n        .error { color: #F00; background-color: #f1f4f3; }\n        div.dialog-hidden { display:none}\n        html, body { margin: 0; padding: 0;}\n    </style>\n    <!-- Global JavaScript -->\n    <script type="text/javascript">\n\n        function openWindow(url,text,id){\n            var $dialog = $(\'<div></div>\').html(\'<div id="\'+id+\'" style="margin:10px"></div>\').dialog({\n                autoOpen: false,\n                modal: true,\n                height:  580,\n                width: 820,\n                resizable: false,\n                draggable: true,\n                position : { my: "center", at: "top", of: window },\n                title: text,\n                buttons: {\n                    "Close": function ()\n                    {\n                        $(this).dialog(\'destroy\').remove();\n                    }\n                }\n            });\n            $dialog.dialog(\'open\');\n        }\n        function openTab(text,url) {\n            var num_tabs = $("div#tabs ul.main1 li.main1").length + 1;\n            var mytext= text;\n            var id = "frame"+num_tabs;\n            $("div#tabs ul.main1").append("<li class=\'main1\'><a href=\'#tab"+num_tabs+"\'>"+mytext+"</a><span class=\'ui-icon ui-icon-close\' role=\'presentation\'>Remove Tab</span></li>");\n            $("div#tabs").append("<div id=\'tab"+num_tabs+"\'> <div class=\'row\'><div class=\'col-lg-12\'><div id=\'"+id+"\' style=\'margin:10px\'>" +\n                    "</div><div id=\'loader"+id+"\' class=\'cygnus\'><span style=\'float:left;width: 20%;\'><p>Cargando ...</p>" +\n                    "</span><span style=\'float:right;width: 80%;\'><img src=')
        __M_writer(escape(tg.url('/img/loader.gif')))
        __M_writer('></span></div></div></div></div>");\n            var $head = $("#"+id).contents().find("head");\n            var ur="')
        __M_writer(escape(tg.url('/css/theme/jquery-ui1.css')))
        __M_writer('";\n            $head.append($("<link/>", { rel: "stylesheet", href:ur, type: "text/css" }));\n            $("div#tabs").tabs("refresh").tabs(\'option\', \'active\', num_tabs - 1);\n        }\n        $(document).ready(function () {\n            $("div#tabs").tabs();\n            $( "#tabs" ).tabs().on( "click", "span.ui-icon-close", function() {\n              var num_tabs = $("div#tabs ul li").length + 1;\n              var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" );\n              $( "#" + panelId ).remove();\n              $("div#tabs").tabs("refresh").tabs(\'option\', \'active\', num_tabs - 1);\n            });\n        });\n\t</script>\n\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\n</head>\n\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer('">\n')
        __M_writer(escape(self.main_menu()))
        __M_writer('\n')
        __M_writer(escape(self.footer()))
        __M_writer('\n')
        __M_writer(escape(self.bottom_scripts()))
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="Bootstrap 3 App">\n    <meta name="author" content="Jorge Macias & Maria Lacayo">\n    <meta name="keyword" content="Sun">\n    <meta name="viewport" content="initial-scale=1.0">\n    <meta charset="utf-8">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
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
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- INSERT MAIN MENU -->\n<nav>\n      <table style="width: 100%"  class=" ui-tabs-panel ui-corner-bottom ui-widget-content">\n          <td>\n              <ul class="nav nav-tabs ui-widget-header">\n                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>jqGrids Examples</a></li>\n              </ul>\n              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">\n                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">\n                            <button onclick="openTab(\'')
        __M_writer(escape(_('Users')))
        __M_writer("','")
        __M_writer(escape(tg.url('/user')))
        __M_writer('\')" title="Installers">')
        __M_writer(escape(_('Users')))
        __M_writer('</button>\n                      </div>\n              </div>\n          </td>\n      </table>\n</nav>\n      <div id="tabs">\n          <ul class="nav nav-tabs ui-widget-header main1">\n            <li class="main1"><a href="#tabs-1" >Main</a></li>\n          </ul>\n          <div id="tabs-1" align="center">\n            ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n          </div>\n      </div>\n    <!-- End MENU -->\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\n')
        if flash:
            __M_writer('    <script>$.alert("')
            __M_writer(escape(str(tg.flash_obj.pop_payload()['message'])))
            __M_writer('" ,{autoclose:false,type:\'info\',title:false});</script>\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <!-- INSERT FOOTER -->\n    <div class="text-right">\n        <div class="credits">\n              <p>Copyright &copy; Madd Systems ')
        __M_writer(escape(h.current_year()))
        __M_writer('&nbsp;</p>\n        </div>\n    </div>\n')
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
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/master.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 6, "28": 6, "29": 7, "30": 7, "31": 8, "32": 8, "33": 10, "34": 10, "35": 11, "36": 11, "37": 14, "38": 14, "39": 16, "40": 16, "41": 17, "42": 17, "43": 21, "44": 21, "45": 22, "46": 22, "47": 23, "48": 23, "49": 24, "50": 24, "51": 25, "52": 25, "53": 26, "54": 26, "55": 27, "56": 27, "57": 28, "58": 28, "59": 29, "60": 29, "61": 119, "62": 119, "63": 121, "64": 121, "65": 136, "66": 136, "67": 139, "68": 139, "69": 140, "70": 140, "71": 141, "72": 141, "73": 142, "74": 142, "75": 152, "76": 154, "77": 156, "78": 158, "79": 187, "80": 198, "81": 207, "87": 144, "92": 144, "93": 145, "94": 145, "100": 154, "104": 154, "110": 156, "119": 158, "128": 160, "135": 160, "136": 170, "137": 170, "138": 170, "139": 170, "140": 170, "141": 170, "142": 181, "143": 181, "149": 190, "156": 190, "157": 191, "158": 192, "159": 193, "160": 194, "161": 193, "162": 194, "163": 195, "164": 195, "165": 195, "166": 197, "167": 197, "168": 197, "174": 200, "179": 200, "180": 204, "181": 204, "187": 209, "191": 209, "197": 191}}
__M_END_METADATA
"""
