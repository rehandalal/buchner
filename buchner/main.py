from flask import Flask
from flask.ext.funnel import Funnel
from flask.ext.mobility import Mobility
from types import ModuleType, FunctionType

from .errors import register_error_handlers


def create_app(settings):
    """Create a new Flask application"""
    app = Flask(__name__)
    Funnel(app)
    Mobility(app)

    # Import settings from file
    for name in dir(settings):
        value = getattr(settings, name)
        if not (name.startswith('_') or isinstance(value, ModuleType)
                or isinstance(value, FunctionType)):
            app.config[name] = value

    # Register blueprints
    for blueprint in app.config.get('BLUEPRINTS', ()):
        app.register_blueprint(
            getattr(__import__(blueprint, fromlist=['blueprint']), 'blueprint'))

    # Register error handlers
    register_error_handlers(app)

    @app.context_processor
    def context_processor():
        return dict(config=app.config)

    return app
