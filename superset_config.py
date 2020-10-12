import os

# AUTH_TYPE = 1  # Database Authentication
# AUTH_USER_REGISTRATION = True
# AUTH_USER_REGISTRATION_ROLE = "Public"

# Superset specific config
ROW_LIMIT = 5000

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = '\xbf)zw\x12\xf0D\xc8\xe2\xd8!z\xf1c\x1c6t\x0c\x86eo)\x80*'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(os.getenv("PG_USER"),
                                                                        os.getenv("PG_PASSWORD"),
                                                                        os.getenv("PG_HOST"),
                                                                        os.getenv("PG_PORT"),
                                                                        os.getenv("PG_DBNAME")
                                                                        )
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = ['login', 'superset.csrf_token', ]
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 3600
# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

# Grant public role the same set of permissions as for the GAMMA role.
# This is useful if one wants to enable anonymous users to view
# dashboards. Explicit grant on specific datasets is still required.
PUBLIC_ROLE_LIKE_GAMMA = True

SESSION_COOKIE_HTTPONLY = False

SESSION_COOKIE_SAMESITE = None

# RECAPTCHA_USE_SSL = False
# RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC')
# RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE')
# RECAPTCHA_OPTIONS = {'theme': 'white'}
