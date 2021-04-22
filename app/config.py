import os

# set base directory for db
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # secret key for forms security
    SECRET_KEY = os.environ.get("SECRET_KEY") or "some_secret_key"
    
    # database #
    ### NB! ONLY FOR DEVENV ####
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ### NB! ONLY FOR DEVENV #####