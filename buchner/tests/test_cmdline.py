import os
import shutil
from tempfile import mkdtemp
from unittest import TestCase

from nose.tools import eq_

from buchner.cmdline import clean_project_module, cmdline_handler


class TestBuchnerCmd(TestCase):
    def setUp(self):
        super(TestBuchnerCmd, self).setUp()
        self.tempd = mkdtemp(prefix='buchner')
        self._oldcwd = os.getcwd()

    def tearDown(self):
        super(TestBuchnerCmd, self).tearDown()
        if os.path.exists(self.tempd):
            shutil.rmtree(self.tempd)
        os.chdir(self._oldcwd)

    def test_create(self):
        """'bucnher-cmd create' should create project directories"""
        os.chdir(self.tempd)
        cmdline_handler('buchner-cmd', ['create', '--noinput', 'foo'])
        assert os.path.exists(os.path.join(self.tempd, 'foo'))


class TestUtilities(TestCase):
    def test_clean_project_module(self):
        """clean_project_module should generate valid Python module names"""
        for s, e in [
            ('foo', 'foo'),
            ('Foo', 'foo'),
            ('Foo Foo', 'foofoo'),
            ('FOO FOO', 'foofoo'),
            ('ou812', 'ou812'),
            ('8675309', 'eight675309'),
            ('asdf!@#$%^&*()_+', 'asdf'),
            ('asdf\xde\xb4', 'asdf')
            ]:

            eq_(clean_project_module(s), e)
