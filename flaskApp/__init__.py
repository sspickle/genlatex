
import flask
import flask_bootstrap

def create_app(config_filename):
    app = flask.Flask(__name__)
    app.config_from_pyfile(config_filename)

    flask_bootstrap.Bootstrap(app)
    return app


