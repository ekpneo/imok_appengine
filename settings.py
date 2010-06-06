import os, os.path

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

MAP_KEY = 'ABQIAAAAAFc3F2oO92IOeSdh20OvwRTIaxK6J1v0NBsI6tB269QU6Hg_LRSrbrOnRs7NAA_zH6sTW8fJ-5NpgQ'

# Possible values:
# - android: Old phone-based gateway
# - twilio: Twilio-based. Cheap and nice. Use it. Love it. Cherish it. Give it potatoes.
# - google-voice: Google-Voice-based. Defunct -- don't bother.
SMS_PROVIDER = 'twilio'

# Incoming phone number.  Displayed on main profile page.  Override in local_settings.py
SMS_GATEWAY = '555-555-5555'

# Twilio settings -- OVERRIDE IN local_settings.py!!
TWILIO_ACCOUNT_ID = 'ACXXXXXXXXXXXXXX'
TWILIO_AUTH_TOKEN = 'YYYYYYYYYYYYYY'

TWILIO_API_VERSION = '2008-08-01'

HOST = 'yourserver.com'

MAILER_EMAIL = 'imok.mailer@gmail.com'

PERSON_FINDER_URL = 'http://chilepersonfinder.appspot.com/api/write?key=%(key)s'
PERSON_FINDER_DEADLINE_SECONDS = 10

def template_path(template_file):
  return os.path.join(TEMPLATE_DIR, template_file)

try:
  from local_settings import *
except ImportError:
  pass
