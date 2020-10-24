"""
Settings to pass the CI without interfering too much with other env settings
"""

SECRET_KEY = "Hello little wise spy :)"
DEBUG = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600


def execute():
    """Placeholder. Do nothing during ci"""
