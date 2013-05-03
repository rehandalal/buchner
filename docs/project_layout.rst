==============================
 Layout and project structure
==============================

.. Note::

   This needs some work.


This covers the layout and structure of Büchner projects. We also talk
about some of the decisions we made. It's high level. For more
details, read through the skeleton code that ``buchner-tool
createproject ...`` creates.

Here's the layout::

    ./Buildfile
    ./CONTRIBUTORS
    ./node.json
    ./manage.py
    ./bin
    ./bin/yuicompressor-2.4.7.jar
    ./README.rst
    ./Procfile
    ./LICENSE
    ./PROJECTMODULE
    ./PROJECTMODULE/main.py
    ./PROJECTMODULE/wsgi.py
    ./PROJECTMODULE/apps
    ./PROJECTMODULE/apps/sample
    ./PROJECTMODULE/apps/sample/templates
    ./PROJECTMODULE/apps/sample/templates/sample
    ./PROJECTMODULE/apps/sample/templates/sample/index.html
    ./PROJECTMODULE/apps/sample/models.py
    ./PROJECTMODULE/apps/sample/__init__.py
    ./PROJECTMODULE/apps/sample/views.py
    ./PROJECTMODULE/apps/__init__.py
    ./PROJECTMODULE/settings_test.py
    ./PROJECTMODULE/database
    ./PROJECTMODULE/database/classes.py
    ./PROJECTMODULE/database/helpers.py
    ./PROJECTMODULE/database/__init__.py
    ./PROJECTMODULE/errors.py
    ./PROJECTMODULE/templates
    ./PROJECTMODULE/templates/base.html
    ./PROJECTMODULE/templates/errors
    ./PROJECTMODULE/templates/errors/404.html
    ./PROJECTMODULE/templates/errors/base.html
    ./PROJECTMODULE/templates/errors/500.html
    ./PROJECTMODULE/migrations
    ./PROJECTMODULE/migrations/README
    ./PROJECTMODULE/migrations/versions
    ./PROJECTMODULE/migrations/versions/__init__.py
    ./PROJECTMODULE/migrations/migrate.cfg
    ./PROJECTMODULE/migrations/__init__.py
    ./PROJECTMODULE/bundles.py
    ./PROJECTMODULE/__init__.py
    ./PROJECTMODULE/settings_local.py-dist
    ./PROJECTMODULE/settings.py
    ./PROJECTMODULE/tests
    ./PROJECTMODULE/tests/__init__.py
    ./requirements.txt


The project consists of some project scaffolding and then a bunch of
apps. This is primarily in the project root and the top layer of the
``PROJECTMODULE/``.


Helper functions
================

Büchner has some helper functions. So not only does it have the
command to create the project skeleton, but it'll continue to be used
as a library for your project.


Configuration
=============

Project configuration is done in ``PROJECTMODULE/settings.py`` and
server-specific configuration that differs between instances of your
site should be done in ``PROJECTMODULE/settings_local.py``. There's a
``settings_local.py-dist`` template that you can copy over to start
this file.


Error templates
===============

Error templates are in ``PROJECTMODULE/templates/errors/``.


Apps
====

Apps are essentially Flask blueprints that provide site
functionality. App code is in ``PROJECTMODULE/apps/``. See the sample
app for an example.


Database
========

We're using `sqlalchemy <http://www.sqlalchemy.org/>`_ and
`sqlalchemy-migrate <http://code.google.com/p/sqlalchemy-migrate/>`_
for database stuff.

Migrations are in ``PROJECTMODULE/migrations/``.


Creating the initial migration
------------------------------

To create your initial database schema, you need to create the models
in the various places. Then do::

    $ python manage.py new_migration "initial"


That'll create your initial migration. Open that file and copy/paste
your schema definitions into it.

If you have problems, bug Rehan.


CSS
===

We're using `LESS <http://lesscss.org/>`_ for CSS.


Heroku
======

The project root contains files that make it easier to use on Heroku.
