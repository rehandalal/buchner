from . import settings
from .main import create_app

app = create_app(settings)
