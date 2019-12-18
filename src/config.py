import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


app_config = {
    'development': Development,
    'production': Production,
}

FLASK_ENV = 'development'
DATABASE_URL = 'sqlite:////web/Sqlite-Data/blog_api_db.db'
JWT_SECRET_KEY = 'hi'
