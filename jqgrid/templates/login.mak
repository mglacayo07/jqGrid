<%inherit file="local:templates.master"/>
<%def name="title()">
  <title>Login</title>
</%def>

<body>
  <h1>Login</h1>

  <div class="row">
    <div class="col-md-8 col-md-offset-1">
      <form action="${tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))}"
            method="post" accept-charset="UTF-8" class="form-horizontal">
        <div class="form-group">
          <label class="col-sm-2 control-label">Username:</label>
          <div class="col-sm-10">
            <input class="form-control" type="text" name="login" value="${login}"/>
          </div>
        </div>
        <div class="form-group">
          <label class="col-sm-2 control-label">Password:</label>
          <div class="col-sm-10">
            <input class="form-control" type="password" name="password"/>
          </div>
        </div>
        <div class="form-group">
          <div class="col-sm-10 col-sm-offset-2">
            <div class="checkbox">
              <label>
                <input type="checkbox" name="remember" value="2252000" /> remember me
              </label>
            </div>
          </div>
        </div>
        <div class="form-group">
          <div class="col-sm-10 col-sm-offset-2">
            <button type="submit" class="btn btn-default">Login</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</body>
