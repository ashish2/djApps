import os
from settings import DATABASES

# Settings at the End

### Settings for Heroku
import dj_database_url
#DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

heroku_pg_url = 'postgres://ivvmabgfrysfgo:hJJ_2qRdime4SRRH9AeiY-GqYz@ec2-50-17-207-54.compute-1.amazonaws.com:5432/df4n1vasgl12gv'
heroku_pg_url = "postgres://ezvnjwuahvqkbn:0EcFmNpePt3ARLBAOjiyDH9rwx@ec2-54-204-35-207.compute-1.amazonaws.com:5432/d6lgoemjjf1emo"

# New For this app
#HEROKU_POSTGRESQL_PUCE_URL
#postgresql-reticulated-9660
#/

DATABASES = {'default': dj_database_url.config(default=heroku_pg_url)}

# honor the 'x_forwarded_proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all hosts headers
ALLOW_HOST = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
#STATIC_ROOT = 'static_root'
#STATIC_URL = '/static/'

current_dir = os.path.dirname( __file__ )

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
	current_dir,
)

