DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'TEST_NAME': 'test1.db',
    }
}

ROOT_URLCONF='testapp.urls'

SITE_ID = 1

SECRET_KEY = "not very secret in tests"

ALLOWED_HOSTS = (
    'testserver',
    '*'
)

INSTALLED_APPS = (
    "rest_framework",
    "testapp"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)
