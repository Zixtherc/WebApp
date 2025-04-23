from home import home, render_home
from register import register, render_register

home.add_url_rule(rule = "/", view_func = render_home)
register.add_url_rule(rule = '/register/', view_func = render_register)