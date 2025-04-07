import flask

from home_app import app

project = flask.Flask(
    import_name = 'Project',
    static_folder = 'static',
    template_folder = 'templates',
    static_url_path = '/static/'
)

project.register_blueprint(blueprint = app.home)