
import flask
import flask_bootstrap

def create_app(config_filename = None):
    app = flask.Flask(__name__)
    if config_filename:
        app.config_from_pyfile(config_filename)

    from . import ui

    app.register_blueprint(ui.bp)
    app.add_url_rule('/', endpoint='index')

    flask_bootstrap.Bootstrap(app)
    return app

