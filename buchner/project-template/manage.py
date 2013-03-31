#!/usr/bin/env python
import os

from flask.ext.script import Manager
from flask.ext.funnel.manager import manager as funnel_manager

from migrate.exceptions import DatabaseAlreadyControlledError
from migrate.versioning import api as migrate_api

from PROJECTMODULE.wsgi import app


manager = Manager(app)

# Add the Flask-Funnel manager as a submanager
manager.add_command('funnel', funnel_manager)

app_path = os.path.join(os.path.dirname(__file__), 'PROJECTMODULE')
db_repo = os.path.join(app_path, 'migrations')
db_url = app.config.get('DATABASE_URL')


def get_db_version():
    """Returns the current version of the database"""
    return migrate_api.db_version(url=db_url, repository=db_repo)


@manager.command
def db_create():
    """Create the database"""
    try:
        migrate_api.version_control(url=db_url, repository=db_repo)
        db_upgrade()
    except DatabaseAlreadyControlledError:
        print 'ERROR: Database is already version controlled.'


@manager.command
def db_downgrade(version):
    """Downgrade the database"""
    v1 = get_db_version()
    migrate_api.downgrade(url=db_url, repository=db_repo, version=version)
    v2 = get_db_version()

    if v1 == v2:
        print 'No changes made.'
    else:
        print 'Downgraded: %s ... %s' % (v1, v2)


@manager.command
def db_upgrade(version=None):
    """Upgrade the database"""
    v1 = get_db_version()
    migrate_api.upgrade(url=db_url, repository=db_repo, version=version)
    v2 = get_db_version()

    if v1 == v2:
        print 'Database already up-to-date.'
    else:
        print 'Upgraded: %s ... %s' % (v1, v2)


@manager.command
def db_version():
    """Get the current version of the database"""
    print get_db_version()


@manager.command
def new_migration(description):
    """Create a new migration"""
    migrate_api.script(description, db_repo)
    print 'New migration script created.'


if __name__ == '__main__':
    manager.run()
