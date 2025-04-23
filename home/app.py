import flask

home = flask.Blueprint(
    name = "home",
    import_name = __name__,
    static_url_path = "/home_app/",
    static_folder = "static",
    template_folder = "templates"
)
