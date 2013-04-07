====================
 Hacking on Büchner
====================

Hack!
=====

Do this:

1. create a `Python virtual environment
   <https://pypi.python.org/pypi/virtualenv>`_
2. (optional) go to https://github.com/rehandalal/buchner and fork it
3. get the source code::

       $ git clone git://github.com/rehandalal/buchner.git

   (or use your fork)
4. install buchner for hacking::

       $ python setup.py develop

5. install other dev requirements::

       $ pip install -r requirements-dev.txt


Test!
=====

Tests are located in ``buchner/tests/``. We use `nose
<https://nose.readthedocs.org/en/latest/>`_.

To run the tests::

    $ nosetests


Document!
=========

Documentation is located in ``docs/``. We use `Sphinx
<http://sphinx-doc.org/>`_.

To build the docs in html::

    $ cd docs
    $ make html
