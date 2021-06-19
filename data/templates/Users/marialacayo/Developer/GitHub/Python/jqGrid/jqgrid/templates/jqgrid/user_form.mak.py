# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1624072097.81852
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/jqgrid/user_form.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/jqgrid/user_form.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        id = context.get('id', UNDEFINED)
        user_id = context.get('user_id', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<form id="form')
        __M_writer(escape(id))
        __M_writer('" action="')
        __M_writer(escape(h.url()))
        __M_writer(escape(id))
        __M_writer('/save">\n    <input hidden type="text" id="user_id_')
        __M_writer(escape(id))
        __M_writer('"  name="user_id_')
        __M_writer(escape(id))
        __M_writer('" value=\'')
        __M_writer(escape(user_id))
        __M_writer("'>\n    <fieldset>\n        <legend>")
        __M_writer(escape(_('User Data')))
        __M_writer(' </legend>\n        <table style="width:100%">\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('User Name')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="user_name_')
        __M_writer(escape(id))
        __M_writer('" name="user_name_')
        __M_writer(escape(id))
        __M_writer('" value=\'')
        __M_writer(escape(user.user_name))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Email Address')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="email_address_')
        __M_writer(escape(id))
        __M_writer('" name="email_address_')
        __M_writer(escape(id))
        __M_writer('" value=\'')
        __M_writer(escape(user.email_address))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Display Name')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="display_name_')
        __M_writer(escape(id))
        __M_writer('" name="display_name_')
        __M_writer(escape(id))
        __M_writer('" value=\'')
        __M_writer(escape(user.display_name))
        __M_writer('\'>\n                </td>\n            </tr>\n            <tr style="height: 10px">\n                <td></td>\n            </tr>\n            <tr>\n                <td>\n                    ')
        __M_writer(escape(_('Password')))
        __M_writer(':\n                </td>\n                <td>\n                    <input type="text" id="password_')
        __M_writer(escape(id))
        __M_writer('" name="password_')
        __M_writer(escape(id))
        __M_writer('" >\n                </td>\n            </tr>\n        </table>\n    </fieldset>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/jqgrid/user_form.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/jqgrid/user_form.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "27": 1, "28": 1, "29": 1, "30": 1, "31": 1, "32": 1, "33": 2, "34": 2, "35": 2, "36": 2, "37": 2, "38": 2, "39": 4, "40": 4, "41": 8, "42": 8, "43": 11, "44": 11, "45": 11, "46": 11, "47": 11, "48": 11, "49": 19, "50": 19, "51": 22, "52": 22, "53": 22, "54": 22, "55": 22, "56": 22, "57": 30, "58": 30, "59": 33, "60": 33, "61": 33, "62": 33, "63": 33, "64": 33, "65": 41, "66": 41, "67": 44, "68": 44, "69": 44, "70": 44, "76": 70}}
__M_END_METADATA
"""
