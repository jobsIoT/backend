import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:290442@localhost:5432/test_iot'

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
