try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-uuidfield').version
except Exception:
    VERSION = 'unknown'
    
from .fields import UUIDField
