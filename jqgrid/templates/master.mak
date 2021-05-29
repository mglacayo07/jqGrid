<!DOCTYPE html>
<html>
<head>
    ${self.meta()}

    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-1.11.0.js')}"></script>
    <script src="${tg.url('/lib/js/bootstrap.min.js')}"></script>
    <script type="text/ecmascript" src="${tg.url('/lib/js/grid.locale-es.js')}"></script>
    <!-- This is the Javascript file of jqGrid -->
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery.jqgrid.src.js')}"></script>
    <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-ui.min.js')}"></script>
    <!-- This is the localization file of the grid controlling messages, labels, etc.
    A link to a jQuery UI ThemeRoller theme, more than 22 built-in and many more custom -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/jquery-ui.css')}" />
    <!-- The link to the CSS that the grid needs -->
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/lib/css/ui.jqgrid.css')}"  />
    <link href="${tg.url('/lib/fonts/font-awesome.min.css')}" rel="stylesheet" />
    <meta charset="utf-8" />
    <title>jqGrid</title>

    <link href="${tg.url('/lib/css/bootstrap.min.css')}" rel="stylesheet">
    <script src="${tg.url('/lib/stomp/stomp.js')}"></script>
    <script src="${tg.url('/lib/moment/moment.js')}"></script>
    <script src="${tg.url('/lib/js/alert.js')}"></script>
    <script src="${tg.url('/lib/justgage/raphael-2.1.4.min.js')}"></script>
    <script src="${tg.url('/lib/justgage/justgage.js')}"></script>
    <script src="${tg.url('/lib/jqueryrotate/jQueryRotate.js')}"></script>
    <script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
    <script src="${tg.url('/lib/timepicker/jquery-ui-timepicker-addon.js')}"></script>

    <style type="text/css">
        .dropdown {
          background: rgba(255, 255, 255, 0.1);
          float: left;
          margin: 10px 8px;
          padding: 0px;
          border-radius: 4px;
          list-style-type: none;}
        .dropdown a.dropdown-toggle {
          height: 40px;
          width: 40px;
          padding-top: 11px;
          padding-left: 9px; }
        .dropdown:hover {
          color: #fff;
          background: rgba(255, 255, 255, 0.2); }
        .dropdown .label {
          top: -4px;
          left: 22px;
          padding-top: 4px;
          padding-bottom: 4px;
          position: absolute;
          border-radius: 9999px; }
        .profile-sidebar {
          padding: 10px 0;
          border-bottom: 1px solid #e9ecf2; }
        .label-success {
          background-color: #8ad919; }
        .label-danger {
          background-color: #f9243f; }
        .profile-userpic img {
          float: left;
          margin: 10px 0px 0px 15px;
          width: 50px;
          height: 50px;
          border-radius: 9999px !important; }
        .profile-usertitle {
          float: left;
          text-align: left;
          margin: 10px 0 0 12px; }
        .profile-usertitle-name {
          font-size: 15px;
          margin-bottom: 0px; }
        .profile-usertitle-status {
          text-transform: uppercase;
          color: #AAA;
          font-size: 10px;
          font-weight: 600;
          margin-bottom: 15px; }
        .indicator {
          width: 10px;
          height: 10px;
          display: inline-block;
          border-radius: 9999px;
          margin-right: 5px; }
        .error { color: #F00; background-color: #f1f4f3; }
        div.dialog-hidden { display:none}
        html, body { margin: 0; padding: 0;}
    </style>
    <!-- Global JavaScript -->
    <script type="text/javascript">

        function openWindow(url,text,id){
            var $dialog = $('<div></div>').html('<div id="'+id+'" style="margin:10px"></div>').dialog({
                autoOpen: false,
                modal: true,
                height:  580,
                width: 820,
                resizable: false,
                draggable: true,
                position : { my: "center", at: "top", of: window },
                title: text,
                buttons: {
                    "Close": function ()
                    {
                        $(this).dialog('destroy').remove();
                    }
                }
            });
            $dialog.dialog('open');
        }
        function openTab(text,url) {
            var num_tabs = $("div#tabs ul.main1 li.main1").length + 1;
            var mytext= text;
            var id = "frame"+num_tabs;
            $("div#tabs ul.main1").append("<li class='main1'><a href='#tab"+num_tabs+"'>"+mytext+"</a><span class='ui-icon ui-icon-close' role='presentation'>Remove Tab</span></li>");
            $("div#tabs").append("<div id='tab"+num_tabs+"'> <div class='row'><div class='col-lg-12'><div id='"+id+"' style='margin:10px'>" +
                    "</div><div id='loader"+id+"' class='cygnus'><span style='float:left;width: 20%;'><p>Cargando ...</p>" +
                    "</span><span style='float:right;width: 80%;'><img src=${tg.url('/img/loader.gif')}></span></div></div></div></div>");
            var $head = $("#"+id).contents().find("head");
            var ur="${tg.url('/css/theme/jquery-ui1.css')}";
            $head.append($("<link/>", { rel: "stylesheet", href:ur, type: "text/css" }));
            $("div#tabs").tabs("refresh").tabs('option', 'active', num_tabs - 1);
        }
        $(document).ready(function () {
            $("div#tabs").tabs();
            $( "#tabs" ).tabs().on( "click", "span.ui-icon-close", function() {
              var num_tabs = $("div#tabs ul li").length + 1;
              var panelId = $( this ).closest( "li" ).remove().attr( "aria-controls" );
              $( "#" + panelId ).remove();
              $("div#tabs").tabs("refresh").tabs('option', 'active', num_tabs - 1);
            });
        });
	</script>

    ${self.head_content()}
</head>

<body class="${self.body_class()}">
${self.main_menu()}
${self.footer()}
${self.bottom_scripts()}

<%def name="meta()">
    <meta charset="${response.charset}" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Bootstrap 3 App">
    <meta name="author" content="Jorge Macias & Maria Lacayo">
    <meta name="keyword" content="Sun">
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
</%def>

<%def name="title()">  </%def>

<%def name="head_content()"></%def>

<%def name="body_class()"></%def>

<%def name="main_menu()">
  <!-- INSERT MAIN MENU -->
<nav>
      <table style="width: 100%"  class=" ui-tabs-panel ui-corner-bottom ui-widget-content">
          <td>
              <ul class="nav nav-tabs ui-widget-header">
                  <li class=active><a href="#pl11" aria-expanded=&#34;true&#34;>jqGrids Examples</a></li>
              </ul>
              <div class="tab-content ui-tabs-panel ui-corner-bottom ui-widget-content">
                      <div class="tab-pane fade in active" id="pl11" style="height:70px;padding: 10px">
                            <button onclick="openTab('${_('Users')}','${tg.url('/user')}')" title="Installers">${_('Users')}</button>
                      </div>
              </div>
          </td>
      </table>
</nav>
      <div id="tabs">
          <ul class="nav nav-tabs ui-widget-header main1">
            <li class="main1"><a href="#tabs-1" >Main</a></li>
          </ul>
          <div id="tabs-1" align="center">
            ${self.content_wrapper()}
          </div>
      </div>
    <!-- End MENU -->


</%def>


<%def name="content_wrapper()">
  <%
    flash=tg.flash_obj.render('flash', use_js=False)
  %>
  % if flash:
    <script>$.alert("${str(tg.flash_obj.pop_payload()['message'])}" ,{autoclose:false,type:'info',title:false});</script>
  % endif
  ${self.body()}
</%def>

<%def name="footer()">
   <!-- INSERT FOOTER -->
    <div class="text-right">
        <div class="credits">
              <p>Copyright &copy; Madd Systems ${h.current_year()}&nbsp;</p>
        </div>
    </div>
</%def>

<%def name="bottom_scripts()">
 <script type="text/javascript">

 </script>
</%def>