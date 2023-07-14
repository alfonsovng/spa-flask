from flask import Flask
from flask_login import LoginManager

def __create_logger():
    import logging
    from flask.logging import default_handler
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(default_handler)
    return logger

logger = __create_logger()

login_manager = LoginManager()

def create_app():
    # Construct the core app object
    app = Flask(__name__, instance_relative_config=False)

    app.url_map.strict_slashes = False # https://stackoverflow.com/a/33285603
    app.config.from_object("config.Config")

    app.logger.info("APP is starting!")

    # Initialize Plugins
    login_manager.init_app(app)

    with app.app_context():
        from . import routes_main, routes_auth

        # Register Blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)

        return app