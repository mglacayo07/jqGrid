<script>
    $(window).on("resize", function () {
        var $grid = $("#jqGridUser"),newWidth = $grid.closest(".ui-jqgrid").parent().width();
        $grid.jqGrid("setGridWidth", newWidth, true);
    });
    var grid_name = '#jqGridUser';
    var grid_pager= '#listPagerUser';
    var update_url= "${tg.url('/user/updateGrid')}";
    var load_url  = "${tg.url('/user/loadGrid')}";

    var addParams = {left: 0,width: window.innerWidth-700,top: 20,height: 190,url: update_url,mtype: 'GET', closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
    var editParams = {left: 0,width: window.innerWidth-700,top: 20,height: 200,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,modal: true, width: "500",editfunc: function (rowid) {} };
    var deleteParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
    var viewParams = {left: 0,width: window.innerWidth-700,top: 20,height: 130,url: update_url,mtype: 'GET',closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true};
    var searchParams = {top: 20,height: 130,width: "500",closeAfterAdd: true,closeAfterEdit: true,closeAfterSearch:true,url: update_url,modal: true};
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
        });
        grid.jqGrid('filterToolbar',{stringResult: true,searchOnEnter : false});
        grid.jqGrid('navGrid',grid_pager,{edit:false,add:false,del:false, search:true}, editParams, addParams, deleteParams, searchParams, viewParams);
    });
</script>

    <!-- page start-->
<div id="dialogUser"  title="${_('Users')}"></div>
    <!-- JQGRID table start-->
    <table style="width:100%">
    <table id="jqGridUser" class="scroll" cellpadding="0" cellspacing="0"></table>
    <div id="listPagerUser" class="scroll" style="text-align:center;"></div>
    </table>
    <br>
  <!-- page end-->