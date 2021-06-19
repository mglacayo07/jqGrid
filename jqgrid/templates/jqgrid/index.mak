<script>
    $(window).on("resize", function () {
        var $grid = $("#jqGrid${id}"),newWidth = $grid.closest(".ui-jqgrid").parent().width();
        $grid.jqGrid("setGridWidth", newWidth, true);
    });
    var grid_name = '#jqGrid${id}';
    var grid_pager = '#listPager${id}';
    var load_url  = "${h.url()}/${id}/loadGrid";

    var grid = jQuery(grid_name);
    $(document).ready(function () {
        grid.jqGrid({
            url: load_url,
            datatype: 'json',
            mtype: 'GET',
            colModel: [
                {label:'ID',name: '${key}',index: '${key}', align: 'center',key:true,hidden: false,editable: false,edittype: 'text',search:true,width:40},
                % for item in colModel:
                    {label:'${item['label']}',name: '${item['index']}',index: '${item['index']}', align: '${item['align']}',hidden: ${item['hidden']},editable: ${item['editable']},edittype: '${item['edittype']}',search:${item['search']}},
                % endfor
            ],
            pager: jQuery(grid_pager),
            rowNum: 16,
            rowList: [16, 50, 100],
            sortname: '${key}',
            sortorder: "${sortorder}",
            viewrecords: true,
            autowidth: true,
            multiselect: ${multi},
            height: 250,
            ondblClickRow: function(rowId) {
                actions${id}(rowId, "update")
            }
        });
        grid.jqGrid('filterToolbar',{stringResult: true,searchOnEnter : false});
        grid.jqGrid('navGrid',grid_pager,{edit:false,add:false,del:false, search:true});

        grid.navButtonAdd(grid_pager, {
            buttonicon: "ui-icon-trash",
            title: "${_('Delete')}",
            caption: "${_('Delete')}",
            position: "first",
            onClickButton: function(){
                var selRowId = grid.jqGrid ('getGridParam', 'selrow');
                var id = grid.jqGrid('getCell',selRowId,'${key}');
                if (id == false){
                    $.alert("${_('No selected row')}",{type: "warning"});
                }else{
                    deleteRow${id}(id, "delete");
                }
            }
        });

        grid.navButtonAdd(grid_pager, {
            buttonicon: "ui-icon-pencil",
            title: "${_('Edit')}",
            caption: "${_('Edit')}",
            position: "first",
            onClickButton: function(){
                var selRowId = grid.jqGrid ('getGridParam', 'selrow');
                var id = grid.jqGrid('getCell',selRowId,'${key}');
                if (id == false){
                    $.alert("${_('No selected row')}",{type: "warning"});
                }else{
                    actions${id}(id, "update")
                }
            }
        });

        grid.navButtonAdd(grid_pager, {
            buttonicon: "ui-icon-plus",
            title: "${_('Add')}",
            caption: "${_('Add')}",
            position: "first",
            onClickButton: function(){
                actions${id}(0,"add")
            }
        });
    });
</script>
<script>
    function deleteRow${id} (rowId,action){
        $('<div></div>').appendTo('body').html('<div><h6>Are you sure you want to delete this user?</h6></div>')
                .dialog({
                    modal: true, title: 'Delete', zIndex: 10000, autoOpen: true,
                    width: 'auto', resizable: false,
                    buttons: {
                        Yes: function () {
                            $.ajax({
                                type: "GET",
                                url: "${h.url()}/${id}/save",
                                contentType: "application/json; charset=utf-8",
                                data: {
                                    '${key}_${id}': rowId,
                                    'action': action
                                },
                                success: function (data) {
                                    // data.value is the success return json. json string contains key value
                                    $('#jqGrid${id}').trigger('reloadGrid');
                                },
                                error: function () {
                                    //alert("#"+ckbid);
                                    $.alert("${_('Error accessing to')} /${id}/save", {
                                        autoClose: false,
                                        type: "danger"
                                    });
                                    return true;
                                },
                                complete: function () {
                                }
                            });
                            $(this).dialog("close");
                        },
                        No: function () {
                            $(this).dialog("close");
                        }
                    },
                    close: function (event, ui) {
                        $(this).remove();
                    }
                });
    }
    function actions${id}(rowId,action) {

        $.ajax({
            type: "GET",
            url: "${h.url()}${id}/open",
            contentType: "application/json; charset=utf-8",
            data: {'${key}':rowId},
            success: function (parameterdata) {
                //Insert HTML code
                $("#dialog${id}").html(parameterdata.dialogtemplate);
                $("#dialog${id}").show();
            },
            error: function () {
                $.alert("${_('Error accessing server')} /${id}/open", {type: "danger"});
            },
            complete: function () {
            }
        });

        var ContDialog = $("#dialog${id}").dialog({
            autoOpen: false,
            height: Math.round(window.innerHeight * .52),
            width: Math.round(window.innerWidth * .35),
            modal: true,
            buttons: {
                "${_('Add')}": function () {
                    if ($("#form${id}").valid()) {
                        var info = $('#form${id}').serialize();
                        $.ajax({
                            type: "GET",
                            url: "${h.url()}${id}/save?"+info,
                            contentType: "application/json; charset=utf-8",
                            data: {'action':action},
                            success: function (data) {
                                // data.value is the success return json. json string contains key value
                                $('#jqGrid${id}').trigger('reloadGrid');
                            },
                            error: function () {
                                //alert("#"+ckbid);
                                $.alert("${_('Error accessing to')} /${id}/save", {autoClose: false, type: "danger"});
                                return true;
                            },
                            complete: function () {
                            }
                        });
                        $('#form${id}')[0].reset();
                        ContDialog.dialog("close");
                    }
                },
                "${_('Close')}": function () {
                    $('#form${id}')[0].reset();
                    ContDialog.dialog("close");
                }
            },
            close: function () {
                $('#form${id}')[0].reset();
            }
        });

        ContDialog.dialog("open");
    }
</script>
<div id="dialog${id}"  title="${id}"></div>

<table style="width:100%">
    <table id="jqGrid${id}" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPager${id}" class="scroll" style="text-align:center;"></div>
</table>