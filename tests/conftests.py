from django.conf import settings
settings.configure(
    DEBUG_PROPAGATE_EXCEPTIONS=True,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                           'NAME': ':memory:'}},
    SITE_ID=1,
    SECRET_KEY='not very secret in tests',
    USE_I18N=True,
    USE_L10N=True,
    STATIC_URL='/static/',
    ROOT_URLCONF='tests.urls',
    ALLOWED_HOSTS=(
        'testserver',
    ),
    TEMPLATE_LOADERS=(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'rest_framework',
        'tests',
    ),
    PASSWORD_HASHERS=(
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ),
)
# guardian is optional
try:
    import guardian # NOQA
except ImportError:
    pass
else:
    settings.ANONYMOUS_USER_ID = -1
    settings.AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'guardian.backends.ObjectPermissionBackend',
    )
    settings.INSTALLED_APPS += (
        'guardian',
    )
    try:
        import django
        django.setup()
    except AttributeError:
        pass


