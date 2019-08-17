from .base import *
import dj_database_url
import django_heroku

DEBUG=False

DATABASES = {
    'default': dj_database_url.config(
      default = config('DATABASE_URL'))
}
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]
django_heroku.settings(locals())

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)