=========
 Büchner
=========

A boilerplate for larger, modular Flask applications.

:code:          https://github.com/rehandalal/buchner/
:issues:        https://github.com/rehandalal/buchner/issues
:license:       BSD 3-clause
:documentation: http://buchner.rtfd.org/
:quickstart:    http://buchner.rtfd.org/en/latest/quickstart.html


Quickstart
==========

This covers how to get up and running with Büchner.

You probably want to install it system-wide since you'll be using
it to create new Flask projects.

Run::

    pip install buchner

After you install it, you can use Büchner to create new Flask-based
projects::

    buchner-tool createproject <PROJECTNAME>

It'll create the project skeleton in the current working directory. You
can run your project immediately::

    $ cd <PROJECTMODULE>
    $ mkvirtualenv <ENVNAME>
    $ pip install -r requirements.txt
    $ python manage.py runserver

Open browser and view ``http://127.0.0.1:5000/``.

Now you have a project skeleton for your new project!


Contents
========

.. toctree::
   :maxdepth: 1

   project_layout
   hacking
