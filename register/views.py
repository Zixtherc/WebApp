import flask

def render_register():
    return flask.render_template(template_name_or_list = 'register.html')