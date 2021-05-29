# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1622136467.388743
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/error.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/error.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        message = context.get('message', UNDEFINED)
        code = context.get('code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n                      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n\n<head>\n  <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>\n  <title>A ')
        __M_writer(escape(code))
        __M_writer(' Error has Occurred </title>\n</head>\n\n<body>\n<h1>Error ')
        __M_writer(escape(code))
        __M_writer('</h1>\n\n')

        import re
        mf = re.compile(r'(</?)script', re.IGNORECASE)
        def fixmessage(message):
            return mf.sub(r'\1noscript', message)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mf','re','fixmessage'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<div>')
        __M_writer(fixmessage(message) )
        __M_writer('</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/error.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/error.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 7, "26": 7, "27": 11, "28": 11, "29": 13, "30": 14, "31": 15, "32": 16, "33": 17, "34": 18, "35": 19, "38": 18, "39": 20, "40": 20, "46": 40}}
__M_END_METADATA
"""
