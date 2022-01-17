import os

SECRET_KEY = '3f3d1f625626d2c76ec126bf5cbca7a8'

FB_APP_ID = 1073090433547074

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')