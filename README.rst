Büchner
=======

A boilerplate for larger, modular Flask applications.

:code:          https://github.com/rehandalal/buchner/
:issues:        https://github.com/rehandalal/buchner/issues
:license:       BSD 3-clause
:documentation: http://buchner.rtfd.org/


Requirements
============

* Python 2.7


Install
=======

Install it with pip::

    $ pip install buchner


Install it from source::

    $ git clone git://github.com/rehandalal/buchner
    $ cd buchner
    $ python setup.py install


Install it for hacking on::

    $ git clone git://github.com/rehandalal/buchner
    $ cd buchner
    $ python setup.py develop


Create a project
================

Once you have it installed, you can create a new project::

    $ buchner-cmd createproject <PROJECTNAME>


It'll create the project skeleton in the current working directory. You
can run your project immediately::

    $ cd <PROJECTMODULE>
    $ mkvirtualenv
    $ pip install -r requirements.txt
    $ python manage.py runserver

    Open browser and view http://127.0.0.1:5000/


Run tests
=========

You need to install the development requirements::

    $ pip install -r requirements-dev.txt


After that, you can run tests with::

    nosetests
