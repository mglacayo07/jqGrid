# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1623553804.2538931
_enable_loop = True
_template_filename = '/jqgrid/templates/loadingData/form.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/dataBase/form.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        user_id = context.get('user_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<form id="formDataBase" action="')
        __M_writer(escape(tg.url('/dataBase/save')))
        __M_writer('">\n    <input hidden type="text" id="user_id_database" value=\'')
        __M_writer(escape(user_id))
        __M_writer("'>\n    <fieldset>\n        <legend>")
        __M_writer(escape(_('User Data')))
        __M_writer(' </legend>\n        <table style="width:100%">\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('User Name')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="user_name_database" name="user_name_database" value=\'')
        __M_writer(escape(user.user_name))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Email Address')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="email_address_database" name="email_address_database" value=\'')
        __M_writer(escape(user.email_address))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Display Name')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="display_name_database" name="display_name_database" value=\'')
        __M_writer(escape(user.display_name))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Password')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="password_database" name="password_database" >\n                </td>\n            </tr>\n        </table>\n    </fieldset>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/dataBase/form.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/dataBase/form.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "26": 1, "27": 1, "28": 1, "29": 2, "30": 2, "31": 4, "32": 4, "33": 8, "34": 8, "35": 11, "36": 11, "37": 19, "38": 19, "39": 22, "40": 22, "41": 30, "42": 30, "43": 33, "44": 33, "45": 41, "46": 41, "52": 46}}
__M_END_METADATA
"""
