import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'

    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/form_management_db'

    DEBUG = os.environ.get('DEBUG') or True



# You can add configurations for different environments like production or testing if needed.
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
