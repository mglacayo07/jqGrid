# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1622948555.212031
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/database.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/database.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script>\n    $(window).on("resize", function () {\n        var $grid = $("#jqGridDataBase"),newWidth = $grid.closest(".ui-jqgrid").parent().width();\n        $grid.jqGrid("setGridWidth", newWidth, true);\n    });\n    var grid_name = \'#jqGridDataBase\';\n    var grid_pager= \'#listPagerDataBase\';\n    var update_url= "')
        __M_writer(escape(tg.url('/dataBase/updateGrid')))
        __M_writer('";\n    var load_url  = "')
        __M_writer(escape(tg.url('/dataBase/loadGrid')))
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
        __M_writer('\'],\n            colModel: [\n                {name: \'user_id\',index: \'user_id\', align: \'center\',key:true,hidden: false,width:20, editable: false,edittype: \'text\',editrules: {required: true},search:false},\n                {name: \'user_name\', index: \'user_name\',align: \'left\',hidden: false, width:70,editable: true, edittype: \'text\', editrules: {required: true}},\n                {name: \'email_address\',index: \'email_address\', align: \'left\',hidden: false,editable: true, edittype: \'text\',editrules: {required: true}},\n                {name: \'display_name\',index: \'display_name\',hidden:false,align: \'left\',editable: true,edittype: \'date\',editrules: {required: true}},\n                {name: \'created\',index: \'internal_id\', align: \'left\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n            ],\n            pager: jQuery(grid_pager),\n            rowNum: 16,\n            rowList: [16, 50, 100],\n            sortname: \'user_id\',\n            sortorder: "asc",\n            viewrecords: true,\n            autowidth: true,\n            height: 250,\n            ondblClickRow: function(rowId) {\n                actionsDataBase(rowId,"update")\n            }\n        });\n        grid.jqGrid(\'filterToolbar\',{stringResult: true,searchOnEnter : false});\n        grid.jqGrid(\'navGrid\',grid_pager,{edit:false,add:false,del:false, search:true}, editParams, addParams, deleteParams, searchParams, viewParams);\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-trash",\n            title: "')
        __M_writer(escape(_('Delete')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Delete')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                var selRowId = grid.jqGrid (\'getGridParam\', \'selrow\');\n                var user_id = grid.jqGrid(\'getCell\',selRowId,\'user_id\');\n                if (user_id == false){\n                    $.alert("')
        __M_writer(escape(_('No selected row')))
        __M_writer('",{type: "warning"});\n                }else{\n                    actionsDataBase(user_id,"delete")\n                }\n            }\n        });\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-pencil",\n            title: "')
        __M_writer(escape(_('Edit')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Edit')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                var selRowId = grid.jqGrid (\'getGridParam\', \'selrow\');\n                var user_id = grid.jqGrid(\'getCell\',selRowId,\'user_id\');\n                if (user_id == false){\n                    $.alert("')
        __M_writer(escape(_('No selected row')))
        __M_writer('",{type: "warning"});\n                }else{\n                    actionsDataBase(user_id,"update")\n                }\n            }\n        });\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-plus",\n            title: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                actionsDataBase(0,"add")\n            }\n        });\n    });\n</script>\n<script>\n    function actionsDataBase(rowId,action) {\n\n        $.ajax({\n            type: "GET",\n            url: "')
        __M_writer(escape(tg.url('/dataBase/open')))
        __M_writer('",\n            contentType: "application/json; charset=utf-8",\n            data: {\'user_id\':rowId},\n            success: function (parameterdata) {\n                //Insert HTML code\n                $("#dialogDataBase").html(parameterdata.dialogtemplate);\n                $("#dialogDataBase").show();\n\n                $("#formDataBase").validate({\n                    rules: {\n                        user_name_database: {\n                            required: true, maxlength: 16\n                        },\n                        email_address_database: {\n                            required: true, maxlength: 255\n                        },\n                        display_name_database: {\n                            required: true, maxlength: 255\n                        }\n                    }\n                });\n            },\n            error: function () {\n                $.alert("')
        __M_writer(escape(_('Error accessing server')))
        __M_writer(' /dataBase/forms", {type: "danger"});\n            },\n            complete: function () {\n            }\n        });\n\n        var ContDialog = $("#dialogDataBase").dialog({\n            autoOpen: false,\n            height: Math.round(window.innerHeight * .52),\n            width: Math.round(window.innerWidth * .35),\n            modal: true,\n            buttons: {\n                "')
        __M_writer(escape(_('Add')))
        __M_writer('": function () {\n                    if ($("#formDataBase").valid()) {\n                        var user_id = $(\'#user_id_database\').val();\n                        var user_name = $(\'#user_name_database\').val();\n                        var email_address = $(\'#email_address_database\').val();\n                        var display_name = $(\'#display_name_database\').val();\n                        var password = $(\'#password_database\').val();\n                        $.ajax({\n                            type: "GET",\n                            url: "')
        __M_writer(escape(h.url()))
        __M_writer('/dataBase/save",\n                            contentType: "application/json; charset=utf-8",\n                            data: {\'user_id\': user_id,\'action\':action,\'user_name\': user_name,\'email_address\': email_address,\'display_name\': display_name,\'password\': password},\n                            success: function (data) {\n                                // data.value is the success return json. json string contains key value\n                                $(\'#jqGridDataBase\').trigger(\'reloadGrid\');\n                            },\n                            error: function () {\n                                //alert("#"+ckbid);\n                                $.alert("')
        __M_writer(escape(_('Error accessing to')))
        __M_writer(' /dataBase/save", {autoClose: false, type: "danger"});\n                                return true;\n                            },\n                            complete: function () {\n                            }\n                        });\n                        $(\'#formDataBase\')[0].reset();\n                        ContDialog.dialog("close");\n                    }\n                },\n                "')
        __M_writer(escape(_('Close')))
        __M_writer('": function () {\n                    $(\'#formDataBase\')[0].reset();\n                    ContDialog.dialog("close");\n                }\n            },\n            close: function () {\n                $(\'#formDataBase\')[0].reset();\n            }\n        });\n\n        ContDialog.dialog("open");\n    }\n</script>\n\n\n<div id="dialogDataBase"  title="')
        __M_writer(escape(_('DataBase')))
        __M_writer('"></div>\n\n<table style="width:100%">\n    <table id="jqGridDataBase" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerDataBase" class="scroll" style="text-align:center;"></div>\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/database.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/database.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 8, "27": 8, "28": 9, "29": 9, "30": 22, "31": 22, "32": 22, "33": 22, "34": 22, "35": 22, "36": 22, "37": 22, "38": 22, "39": 22, "40": 47, "41": 47, "42": 48, "43": 48, "44": 54, "45": 54, "46": 63, "47": 63, "48": 64, "49": 64, "50": 70, "51": 70, "52": 79, "53": 79, "54": 80, "55": 80, "56": 93, "57": 93, "58": 116, "59": 116, "60": 128, "61": 128, "62": 137, "63": 137, "64": 146, "65": 146, "66": 156, "67": 156, "68": 171, "69": 171, "75": 69}}
__M_END_METADATA
"""
