# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1622298001.69177
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/user/user_jqgrid.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/user/user_jqgrid.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script>\n    $(window).on("resize", function () {\n        var $grid = $("#jqGridUser"),newWidth = $grid.closest(".ui-jqgrid").parent().width();\n        $grid.jqGrid("setGridWidth", newWidth, true);\n    });\n    var grid_name = \'#jqGridUser\';\n    var grid_pager= \'#listPagerUser\';\n    var update_url= "')
        __M_writer(escape(tg.url('/user/updateGrid')))
        __M_writer('";\n    var load_url  = "')
        __M_writer(escape(tg.url('/user/loadGrid')))
        __M_writer('";\n\n    var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url,mtype: \'GET\', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};\n    var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true, width: "500",editfunc: function (rowid) {} };\n    var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};\n    var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: \'GET\',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};\n    var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true};\n    var grid = jQuery(grid_name);\n    $(document).ready(function () {\n        grid.jqGrid({\n            url: load_url,\n            datatype: \'json\',\n            mtype: \'GET\',\n            colNames: [\'')
        __M_writer(escape(_('ID')))
        __M_writer("', '")
        __M_writer(escape(_('User')))
        __M_writer("', '")
        __M_writer(escape(_('Email')))
        __M_writer("', '")
        __M_writer(escape(_('Display Name')))
        __M_writer("', '")
        __M_writer(escape(_('Created')))
        __M_writer('\'],\n            colModel: [\n                {name: \'user_id\',index: \'user_id\', align: \'center\',key:true,hidden: false,width:20, editable: false,edittype: \'text\',editrules: {required: true},search:false},\n                {name: \'user_name\', index: \'user_name\',align: \'left\',hidden: false, width:70,editable: true, edittype: \'text\', editrules: {required: true}},\n                {name: \'email_address\',index: \'email_address\', align: \'left\',hidden: false,editable: true, edittype: \'text\',editrules: {required: true}},\n                {name: \'display_name\',index: \'display_name\',hidden:false,align: \'left\',editable: true,edittype: \'date\',editrules: {required: true}},\n                {name: \'created\',index: \'internal_id\', align: \'left\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n            ],\n            pager: jQuery(grid_pager),\n            rowNum: 16,\n            rowList: [16, 50, 100],\n            sortname: \'user_id\',\n            sortorder: "asc",\n            viewrecords: true,\n            autowidth: true,\n            height: 250,\n        });\n        grid.jqGrid(\'filterToolbar\',{stringResult: true,searchOnEnter : false});\n        grid.jqGrid(\'navGrid\',grid_pager,{edit:false,add:false,del:false, search:true}, editParams, addParams, deleteParams, searchParams, viewParams);\n    });\n</script>\n\n    <!-- page start-->\n<div id="dialogUser"  title="')
        __M_writer(escape(_('Users')))
        __M_writer('"></div>\n    <!-- JQGRID table start-->\n    <table style="width:100%">\n    <table id="jqGridUser" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerUser" class="scroll" style="text-align:center;"></div>\n    </table>\n    <br>\n  <!-- page end-->')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/user/user_jqgrid.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/user/user_jqgrid.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 8, "26": 8, "27": 9, "28": 9, "29": 22, "30": 22, "31": 22, "32": 22, "33": 22, "34": 22, "35": 22, "36": 22, "37": 22, "38": 22, "39": 45, "40": 45, "46": 40}}
__M_END_METADATA
"""
