import flask

register = flask.Blueprint(
    name = "register",
    import_name = __name__,
    static_url_path = "/register/",
    static_folder = "static",
    template_folder = "templates"
)