from types import ModuleType, FunctionType

from flask import Flask
from flask.ext.funnel import Funnel
from flask.ext.mobility import Mobility

from PROJECTMODULE.errors import register_error_handlers


def create_app(settings):
    """Create a new Flask application"""
    app = Flask(__name__)

    # Import settings from file
    for name in dir(settings):
        value = getattr(settings, name)
        if not (name.startswith('_') or isinstance(value, ModuleType)
                or isinstance(value, FunctionType)):
            app.config[name] = value

    # Bootstrapping
    if 'INSTALLED_APPS' in app.config:
        app.installed_apps = app.config.get('INSTALLED_APPS', [])

    # Extensions
    Funnel(app)
    Mobility(app)

    # Register blueprints
    for app_path in app.installed_apps:
        app.register_blueprint(
            getattr(__import__('{0}.views'.format(app_path),
                               fromlist=['blueprint']),
                    'blueprint'))

    # Register error handlers
    register_error_handlers(app)

    @app.context_processor
    def context_processor():
        return dict(config=app.config)

    @app.teardown_request
    def teardown_request(exception=None):
        # Remove the database session if it exists
        if hasattr(app, 'db_session'):
            app.db_session.close()

    return app
