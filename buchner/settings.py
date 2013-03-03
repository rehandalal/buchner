import os

from .helpers import truthiness

DEBUG = truthiness(os.environ.get('DEBUG', False))

BLUEPRINTS = ()

try:
    from bundles import *
except ImportError:
    pass

try:
    from settings_local import *
except ImportError:
    pass
