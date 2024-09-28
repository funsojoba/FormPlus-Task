import os



class Config:
    MONGO_URI = (
        'mongodb://' + os.environ.get('MONGODB_USERNAME') 
        + ':'
        + os.environ.get('MONGODB_PASSWORD')
        + '@'
        + os.environ.get('MONGODB_HOSTNAME')
        + ':27017/'
        + os.environ.get('MONGODB_DATABASE')
        + '?authSource=admin&retryWrites=true&w=majority'
    )
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''

    DEBUG = os.environ.get('DEBUG') or True


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
