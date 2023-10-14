from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('NAME_DB'),
        'USER': environ.get('USER_DB'),
        'PASSWORD': environ.get('PASSWORD'),
        'HOST': environ.get('HOST'),
        'PORT': environ.get('PORT')
    }
}
