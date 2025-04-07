from home_app import app, render_home

app.home.add_url_rule(rule= "/", view_func = render_home)