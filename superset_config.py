import os

# Superset specific config
ROW_LIMIT = 5000

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = os.urandom(24)

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'sqlite:////app/.superset/superset.db'
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = ['heroku.com', 'marielle-superset.herokuapp.com']
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 3600

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

SESSION_COOKIE_HTTPONLY = False

SESSION_COOKIE_SAMESITE = 'None'
