# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1623555436.767586
_enable_loop = True
_template_filename = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/jsonData/index.mak'
_template_uri = '/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/jsonData/index.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<script>\n    $(window).on("resize", function () {\n        var $grid = $("#jqGridjsonData"),newWidth = $grid.closest(".ui-jqgrid").parent().width();\n        $grid.jqGrid("setGridWidth", newWidth, true);\n    });\n    var grid_name = \'#jqGridjsonData\';\n    var grid_pager = \'#listPagerjsonData\';\n    var load_url  = "')
        __M_writer(escape(tg.url('/jsonData/jqGridRows')))
        __M_writer('";\n\n    var grid = jQuery(grid_name);\n    $(document).ready(function () {\n        grid.jqGrid({\n            url: load_url,\n            datatype: \'json\',\n            mtype: \'GET\',\n            colNames: [\'')
        __M_writer(escape(_('ID')))
        __M_writer("', '")
        __M_writer(escape(_('User')))
        __M_writer("', '")
        __M_writer(escape(_('Email')))
        __M_writer("', '")
        __M_writer(escape(_('Display Name')))
        __M_writer("', '")
        __M_writer(escape(_('Created')))
        __M_writer('\'],\n            colModel: [\n                {name: \'user_id\',index: \'user_id\', align: \'center\',key:true,hidden: false,width:20, editable: false,edittype: \'text\',editrules: {required: true},search:false},\n                {name: \'user_name\', index: \'user_name\',align: \'left\',hidden: false, width:70,editable: true, edittype: \'text\', editrules: {required: true}},\n                {name: \'email_address\',index: \'email_address\', align: \'left\',hidden: false,editable: true, edittype: \'text\',editrules: {required: true}},\n                {name: \'display_name\',index: \'display_name\',hidden:false,align: \'left\',editable: true,edittype: \'date\',editrules: {required: true}},\n                {name: \'created\',index: \'internal_id\', align: \'left\',hidden: true,editable: true, edittype: \'text\',editrules: {required: false}},\n            ],\n            pager: jQuery(grid_pager),\n            rowNum: 16,\n            rowList: [16, 50, 100],\n            sortname: \'user_id\',\n            sortorder: "asc",\n            viewrecords: true,\n            autowidth: true,\n            height: 250,\n            ondblClickRow: function(rowId) {\n                actionsjsonData(rowId,"update")\n            }\n        });\n        grid.jqGrid(\'filterToolbar\',{stringResult: true,searchOnEnter : false});\n        grid.jqGrid(\'navGrid\',grid_pager,{edit:false,add:false,del:false, search:true});\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-trash",\n            title: "')
        __M_writer(escape(_('Delete')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Delete')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                var selRowId = grid.jqGrid (\'getGridParam\', \'selrow\');\n                var user_id = grid.jqGrid(\'getCell\',selRowId,\'user_id\');\n                if (user_id == false){\n                    $.alert("')
        __M_writer(escape(_('No selected row')))
        __M_writer('",{type: "warning"});\n                }else{\n                    deletejsonData(user_id,"delete");\n                }\n            }\n        });\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-pencil",\n            title: "')
        __M_writer(escape(_('Edit')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Edit')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                var selRowId = grid.jqGrid (\'getGridParam\', \'selrow\');\n                var user_id = grid.jqGrid(\'getCell\',selRowId,\'user_id\');\n                if (user_id == false){\n                    $.alert("')
        __M_writer(escape(_('No selected row')))
        __M_writer('",{type: "warning"});\n                }else{\n                    actionsjsonData(user_id,"update")\n                }\n            }\n        });\n\n        grid.navButtonAdd(grid_pager, {\n            buttonicon: "ui-icon-plus",\n            title: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n            caption: "')
        __M_writer(escape(_('Add')))
        __M_writer('",\n            position: "first",\n            onClickButton: function(){\n                actionsjsonData(0,"add")\n            }\n        });\n    });\n</script>\n<script>\n    function deletejsonData(rowId,action){\n        $(\'<div></div>\').appendTo(\'body\').html(\'<div><h6>Are you sure you want to delete this user?</h6></div>\')\n                .dialog({\n                    modal: true, title: \'Delete\', zIndex: 10000, autoOpen: true,\n                    width: \'auto\', resizable: false,\n                    buttons: {\n                        Yes: function () {\n                            $.ajax({\n                                type: "GET",\n                                url: "')
        __M_writer(escape(h.url()))
        __M_writer('/jsonData/save",\n                                contentType: "application/json; charset=utf-8",\n                                data: {\n                                    \'user_id\': rowId,\n                                    \'action\': action\n                                },\n                                success: function (data) {\n                                    // data.value is the success return json. json string contains key value\n                                    $(\'#jqGridjsonData\').trigger(\'reloadGrid\');\n                                },\n                                error: function () {\n                                    //alert("#"+ckbid);\n                                    $.alert("')
        __M_writer(escape(_('Error accessing to')))
        __M_writer(' /jsonData/save", {\n                                        autoClose: false,\n                                        type: "danger"\n                                    });\n                                    return true;\n                                },\n                                complete: function () {\n                                }\n                            });\n                            $(this).dialog("close");\n                        },\n                        No: function () {\n                            $(this).dialog("close");\n                        }\n                    },\n                    close: function (event, ui) {\n                        $(this).remove();\n                    }\n                });\n    }\n    function actionsjsonData(rowId,action) {\n\n        $.ajax({\n            type: "GET",\n            url: "')
        __M_writer(escape(tg.url('/jsonData/open')))
        __M_writer('",\n            contentType: "application/json; charset=utf-8",\n            data: {\'user_id\':rowId},\n            success: function (parameterdata) {\n                //Insert HTML code\n                $("#dialogjsonData").html(parameterdata.dialogtemplate);\n                $("#dialogjsonData").show();\n\n                $("#formLoadingData").validate({\n                    rules: {\n                        user_name_loading_data: {\n                            required: true, maxlength: 16\n                        },\n                        email_address_loading_data: {\n                            required: true, maxlength: 255\n                        },\n                        display_name_loading_data: {\n                            required: true, maxlength: 255\n                        }\n                    }\n                });\n            },\n            error: function () {\n                $.alert("')
        __M_writer(escape(_('Error accessing server')))
        __M_writer(' /jsonData/jsonData", {type: "danger"});\n            },\n            complete: function () {\n            }\n        });\n\n        var ContDialog = $("#dialogjsonData").dialog({\n            autoOpen: false,\n            height: Math.round(window.innerHeight * .52),\n            width: Math.round(window.innerWidth * .35),\n            modal: true,\n            buttons: {\n                "')
        __M_writer(escape(_('Add')))
        __M_writer('": function () {\n                    if ($("#formLoadingData").valid()) {\n                        var user_id = $(\'#user_id_loading_data\').val();\n                        var user_name = $(\'#user_name_loading_data\').val();\n                        var email_address = $(\'#email_address_loading_data\').val();\n                        var display_name = $(\'#display_name_loading_data\').val();\n                        var password = $(\'#password_loading_data\').val();\n                        $.ajax({\n                            type: "GET",\n                            url: "')
        __M_writer(escape(h.url()))
        __M_writer('/jsonData/save",\n                            contentType: "application/json; charset=utf-8",\n                            data: {\'user_id\': user_id,\'action\':action,\'user_name\': user_name,\'email_address\': email_address,\'display_name\': display_name,\'password\': password},\n                            success: function (data) {\n                                // data.value is the success return json. json string contains key value\n                                $(\'#jqGridjsonData\').trigger(\'reloadGrid\');\n                            },\n                            error: function () {\n                                //alert("#"+ckbid);\n                                $.alert("')
        __M_writer(escape(_('Error accessing to')))
        __M_writer(' /jsonData/save", {autoClose: false, type: "danger"});\n                                return true;\n                            },\n                            complete: function () {\n                            }\n                        });\n                        $(\'#formLoadingData\')[0].reset();\n                        ContDialog.dialog("close");\n                    }\n                },\n                "')
        __M_writer(escape(_('Close')))
        __M_writer('": function () {\n                    $(\'#formLoadingData\')[0].reset();\n                    ContDialog.dialog("close");\n                }\n            },\n            close: function () {\n                $(\'#formLoadingData\')[0].reset();\n            }\n        });\n\n        ContDialog.dialog("open");\n    }\n</script>\n\n\n<div id="dialogjsonData"  title="')
        __M_writer(escape(_('jsonData')))
        __M_writer('"></div>\n\n<table style="width:100%">\n    <table id="jqGridjsonData" class="scroll" cellpadding="0" cellspacing="0"></table>\n    <div id="listPagerjsonData" class="scroll" style="text-align:center;"></div>\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/jsonData/index.mak", "uri": "/Users/marialacayo/Developer/GitHub/Python/jqGrid/jqgrid/templates/loadingData/jsonData/index.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 8, "27": 8, "28": 16, "29": 16, "30": 16, "31": 16, "32": 16, "33": 16, "34": 16, "35": 16, "36": 16, "37": 16, "38": 41, "39": 41, "40": 42, "41": 42, "42": 48, "43": 48, "44": 57, "45": 57, "46": 58, "47": 58, "48": 64, "49": 64, "50": 73, "51": 73, "52": 74, "53": 74, "54": 92, "55": 92, "56": 104, "57": 104, "58": 128, "59": 128, "60": 151, "61": 151, "62": 163, "63": 163, "64": 172, "65": 172, "66": 181, "67": 181, "68": 191, "69": 191, "70": 206, "71": 206, "77": 71}}
__M_END_METADATA
"""
