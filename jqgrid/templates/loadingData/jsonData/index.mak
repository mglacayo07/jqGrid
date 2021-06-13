<script>
    $(window).on("resize", function () {
        var $grid = $("#jqGridjsonData"),newWidth = $grid.closest(".ui-jqgrid").parent().width();
        $grid.jqGrid("setGridWidth", newWidth, true);
    });
    var grid_name = '#jqGridjsonData';
    var grid_pager = '#listPagerjsonData';
    var load_url  = "${tg.url('/jsonData/jqGridRows')}";

    var grid = jQuery(grid_name);
    $(document).ready(function () {
        grid.jqGrid({
            url: load_url,
            datatype: 'json',
            mtype: 'GET',
            colNames: ['${_('ID')}', '${_('User')}', '${_('Email')}', '${_('Display Name')}', '${_('Created')}'],
            colModel: [
                {name: 'user_id',index: 'user_id', align: 'center',key:true,hidden: false,width:20, editable: false,edittype: 'text',editrules: {required: true},search:false},
                {name: 'user_name', index: 'user_name',align: 'left',hidden: false, width:70,editable: true, edittype: 'text', editrules: {required: true}},
                {name: 'email_address',index: 'email_address', align: 'left',hidden: false,editable: true, edittype: 'text',editrules: {required: true}},
                {name: 'display_name',index: 'display_name',hidden:false,align: 'left',editable: true,edittype: 'date',editrules: {required: true}},
                {name: 'created',index: 'internal_id', align: 'left',hidden: true,editable: true, edittype: 'text',editrules: {required: false}},
            ],
            pager: jQuery(grid_pager),
            rowNum: 16,
            rowList: [16, 50, 100],
            sortname: 'user_id',
            sortorder: "asc",
            viewrecords: true,
            autowidth: true,
            height: 250,
            ondblClickRow: function(rowId) {
                actionsjsonData(rowId,"update")
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
                var user_id = grid.jqGrid('getCell',selRowId,'user_id');
                if (user_id == false){
                    $.alert("${_('No selected row')}",{type: "warning"});
                }else{
                    deletejsonData(user_id,"delete");
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
                var user_id = grid.jqGrid('getCell',selRowId,'user_id');
                if (user_id == false){
                    $.alert("${_('No selected row')}",{type: "warning"});
                }else{
                    actionsjsonData(user_id,"update")
                }
            }
        });

        grid.navButtonAdd(grid_pager, {
            buttonicon: "ui-icon-plus",
            title: "${_('Add')}",
            caption: "${_('Add')}",
            position: "first",
            onClickButton: function(){
                actionsjsonData(0,"add")
            }
        });
    });
</script>
<script>
    function deletejsonData(rowId,action){
        $('<div></div>').appendTo('body').html('<div><h6>Are you sure you want to delete this user?</h6></div>')
                .dialog({
                    modal: true, title: 'Delete', zIndex: 10000, autoOpen: true,
                    width: 'auto', resizable: false,
                    buttons: {
                        Yes: function () {
                            $.ajax({
                                type: "GET",
                                url: "${h.url()}/jsonData/save",
                                contentType: "application/json; charset=utf-8",
                                data: {
                                    'user_id': rowId,
                                    'action': action
                                },
                                success: function (data) {
                                    // data.value is the success return json. json string contains key value
                                    $('#jqGridjsonData').trigger('reloadGrid');
                                },
                                error: function () {
                                    //alert("#"+ckbid);
                                    $.alert("${_('Error accessing to')} /jsonData/save", {
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
    function actionsjsonData(rowId,action) {

        $.ajax({
            type: "GET",
            url: "${tg.url('/jsonData/open')}",
            contentType: "application/json; charset=utf-8",
            data: {'user_id':rowId},
            success: function (parameterdata) {
                //Insert HTML code
                $("#dialogjsonData").html(parameterdata.dialogtemplate);
                $("#dialogjsonData").show();

                $("#formLoadingData").validate({
                    rules: {
                        user_name_loading_data: {
                            required: true, maxlength: 16
                        },
                        email_address_loading_data: {
                            required: true, maxlength: 255
                        },
                        display_name_loading_data: {
                            required: true, maxlength: 255
                        }
                    }
                });
            },
            error: function () {
                $.alert("${_('Error accessing server')} /jsonData/jsonData", {type: "danger"});
            },
            complete: function () {
            }
        });

        var ContDialog = $("#dialogjsonData").dialog({
            autoOpen: false,
            height: Math.round(window.innerHeight * .52),
            width: Math.round(window.innerWidth * .35),
            modal: true,
            buttons: {
                "${_('Add')}": function () {
                    if ($("#formLoadingData").valid()) {
                        var user_id = $('#user_id_loading_data').val();
                        var user_name = $('#user_name_loading_data').val();
                        var email_address = $('#email_address_loading_data').val();
                        var display_name = $('#display_name_loading_data').val();
                        var password = $('#password_loading_data').val();
                        $.ajax({
                            type: "GET",
                            url: "${h.url()}/jsonData/save",
                            contentType: "application/json; charset=utf-8",
                            data: {'user_id': user_id,'action':action,'user_name': user_name,'email_address': email_address,'display_name': display_name,'password': password},
                            success: function (data) {
                                // data.value is the success return json. json string contains key value
                                $('#jqGridjsonData').trigger('reloadGrid');
                            },
                            error: function () {
                                //alert("#"+ckbid);
                                $.alert("${_('Error accessing to')} /jsonData/save", {autoClose: false, type: "danger"});
                                return true;
                            },
                            complete: function () {
                            }
                        });
                        $('#formLoadingData')[0].reset();
                        ContDialog.dialog("close");
                    }
                },
                "${_('Close')}": function () {
                    $('#formLoadingData')[0].reset();
                    ContDialog.dialog("close");
                }
            },
            close: function () {
                $('#formLoadingData')[0].reset();
            }
        });

        ContDialog.dialog("open");
    }
</script>


<div id="dialogjsonData"  title="${_('jsonData')}"></div>

<table style="width:100%">
    <table id="jqGridjsonData" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerjsonData" class="scroll" style="text-align:center;"></div>
</table>
