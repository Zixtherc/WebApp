from home_app import app, render_home

from .settings import project


app.home.add_url_rule(rule= "/", view_func = render_home)

project.register_blueprint(blueprint = app.home)