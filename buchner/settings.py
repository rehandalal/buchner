import os

from buchner.helpers import truthiness

def abspath(path):
    return os.path.abspath(os.path.relpath(path, os.path.dirname(__file__)))

DEBUG = truthiness(os.environ.get('DEBUG', False))

DATABASE_URL = os.environ.get('DATABASE_URL')

BLUEPRINTS = ()

# Flask-Funnel
JAVA_BIN = os.environ.get('JAVA_BIN', 'java')

YUI_COMPRESSOR_BIN = os.environ.get('YUI_COMPRESSOR_BIN',
                                    abspath('../bin/yuicompressor-2.4.7.jar'))

LESS_BIN = os.environ.get('LESS_BIN', 'lessc')

try:
    from bundles import *
except ImportError:
    pass

try:
    from settings_local import *
except ImportError:
    pass
