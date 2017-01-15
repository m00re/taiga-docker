# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example

from .common import *
from .original import *

# Set configured database parameters
DATABASES['default']['NAME'] = os.getenv('TAIGA_DB_NAME')
DATABASES['default']['HOST'] = os.getenv('POSTGRES_PORT_5432_TCP_ADDR') or os.getenv('TAIGA_DB_HOST')
DATABASES['default']['USER'] = os.getenv('TAIGA_DB_USER')
DATABASES['default']['PASSWORD'] = os.getenv('POSTGRES_ENV_POSTGRES_PASSWORD') or os.getenv('TAIGA_DB_PASSWORD')
DATABASES['default']['PORT'] = 5432

# Configure hostname and URLs
SITES['api']['domain'] = os.getenv('TAIGA_HOSTNAME')
SITES['front']['domain'] = os.getenv('TAIGA_HOSTNAME')
MEDIA_URL  = 'http://' + os.getenv('TAIGA_HOSTNAME') + '/media/'
STATIC_URL = 'http://' + os.getenv('TAIGA_HOSTNAME') + '/static/'

# If running on SSL externally, change scheme and URLs accordingly
if os.getenv('TAIGA_SSL').lower() == 'true':
    SITES['api']['scheme'] = 'https'
    SITES['front']['scheme'] = 'https'
    MEDIA_URL  = 'https://' + os.getenv('TAIGA_HOSTNAME') + '/media/'
    STATIC_URL = 'https://' + os.getenv('TAIGA_HOSTNAME') + '/static/'

SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')

# Enable or disable public registration
PUBLIC_REGISTER_ENABLED = (os.getenv('TAIGA_PUBLIC_REGISTER_ENABLED').lower() == 'true')

# Enable or disable debugging
DEBUG = (os.getenv('TAIGA_BACKEND_DEBUG').lower() == 'true')
TEMPLATE_DEBUG = (os.getenv('TAIGA_BACKEND_DEBUG').lower() == 'true')
