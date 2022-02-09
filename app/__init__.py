import os
import errno
import logging

from resources.EasyLogger import configure_loggers
from waitress import serve
from flask.logging import default_handler
from flask import Flask


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


root_dir = os.path.normpath(os.getcwd() + os.sep)
make_sure_path_exists(os.path.join(root_dir, "app"))
app_dir = os.path.join(root_dir, "app")
make_sure_path_exists(os.path.join(root_dir, "logs"))
log_dir = os.path.join(app_dir, "logs")


def configure_logging():
    app_logger = logging.getLogger(__name__)
    flask_logger = logging.getLogger("flask")
    waitress_logger = logging.getLogger("waitress")

    configure_loggers(
        [app_logger, flask_logger, waitress_logger], log_to_file=True
    )


def create_app():
    app = Flask(__name__)

    configure_logging()
    return app


app = create_app()


def serve_app(app):
    serve(app, host="0.0.0.0", port=8080, url_scheme="https")


from app import views


if __name__ == "__name__":
    serve_app()
