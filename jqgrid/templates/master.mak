<!DOCTYPE html>

<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta charset="${response.charset}" />



  <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/css/bootstrap.min.css')}" />
  <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/css/style.css')}" />

  <%def name="head()"></%def>
</head>

% if tg.auth_stack_enabled:
  % if h.whoami()=="":
       <meta http-equiv="refresh" content="0; url=${tg.url('/')}" />
  % else:
        <body class="${self.body_class()}">
          ${self.main_menu()}
          ${self.footer()}
        <!-- Insert nice scrool -->
          ${self.bottom_scripts()}
  % endif
% endif

<%def name="title()"> </%def>

<%def name="head_content()"></%def>

<%def name="body_class()"></%def>
  <!-- Navbar -->
<%def name="main_menu()">
  <nav class="navbar navbar-default">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="${tg.url('/')}">
        <img src="${tg.url('/img/yuimx_logo.gif')}" height="20" alt="TurboGears 2"/>
        ${getattr(tmpl_context, 'project_name', 'turbogears2')}
      </a>
    </div>

    <div class="collapse navbar-collapse" id="navbar-content">
      <ul class="nav navbar-nav">
          % if tg.auth_stack_enabled:
                <li><a href="${tg.url('/user')}">JqGrid User</a></li>
          % endif
      </ul>
        % if tg.auth_stack_enabled:
            <ul class="nav navbar-nav navbar-right">
            % if h.whoami()=="":
                <li><a href="${tg.url('/login')}">Login</a></li>
            % else:
                <li><a href="${tg.url('/user')}">JqGrid User</a></li>
                <li><a href="${tg.url('/logout_handler')}">Logout</a></li>
                <li><a href="${tg.url('/admin')}">Admin</a></li>
            % endif
            </ul>
        % endif
    </div>
  </nav>
</%def>
  <%def name="body()"></%def>
  <%def name="content_wrapper()">
    <%
        flash=tg.flash_obj.render('flash', use_js=False)
    %>
    % if flash:
        <script>
            $.alert("${str(tg.flash_obj.pop_payload()['message'])}", { autoclose: false,type: 'info',title: false});
        </script>
    % endif
    ${self.body()}
  </%def>

  <!-- Footer -->
  <%def name="footer()">
      <!-- INSERT FOOTER -->
      <div class="text-right">
          <div class="credits">
              <p>Copyright &copy; Maria Lacayo ${h.current_year()}&nbsp;</p>
          </div>
      </div>
  </%def>

  <script src="http://code.jquery.com/jquery.js"></script>
  <script src="${tg.url('/javascript/bootstrap.min.js')}"></script>
<%def name="bottom_scripts()">
 <script type="text/javascript">

 </script>
</%def>

</html>
