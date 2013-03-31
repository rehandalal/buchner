from types import ModuleType, FunctionType

from flask import Flask
from flask.ext.funnel import Funnel
from flask.ext.mobility import Mobility

from buchner.errors import register_error_handlers


def _get_apps_full_names(apps):
    names = []
    for app in apps:
        parts = []
        if not __name__ == '__main__':
            parts = __name__.split('.')
            parts.pop()
        parts.append('apps')
        parts.append(app)

        names.append('.'.join(parts))
    return names


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
        app.installed_apps = _get_apps_full_names(
            app.config.get('INSTALLED_APPS'))

    # Extensions
    Funnel(app)
    Mobility(app)

    # Register blueprints
    for a in app.installed_apps:
        # Register blueprints
        app.register_blueprint(
            getattr(__import__('%s.views' % a, fromlist=['blueprint']),
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
