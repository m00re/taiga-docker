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

# Configure LDAP backend (if enabled)
if os.getenv('LDAP_ENABLE').lower() == 'true':
    INSTALLED_APPS += ["taiga_contrib_ldap_auth"]
    LDAP_SERVER = os.getenv('LDAP_SERVER')
    LDAP_PORT = int(os.getenv('LDAP_PORT'))
    # Full DN of the service account use to connect to LDAP server and search for login user's account entry
    # If LDAP_BIND_DN is not specified, or is blank, then an anonymous bind is attempated
    LDAP_BIND_DN = os.getenv('LDAP_BIND_DN')
    LDAP_BIND_PASSWORD = os.getenv('LDAP_BIND_PASSWORD')
    # Starting point within LDAP structure to search for login user
    LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCH_BASE')
    # LDAP property used for searching, ie. login username needs to match value in sAMAccountName property in LDAP
    LDAP_SEARCH_PROPERTY = os.getenv('LDAP_SEARCH_PROPERTY')
    LDAP_SEARCH_SUFFIX = None
    # Names of LDAP properties on user account to get email and full name
    LDAP_EMAIL_PROPERTY = os.getenv('LDAP_EMAIL_PROPERTY')
    LDAP_FULL_NAME_PROPERTY = os.getenv('LDAP_FULL_NAME_PROPERTY')
