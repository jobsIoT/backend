import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://tfukrhhhusivup:2a5de14b538622c46b9f616ec77d4977b893ba4b5e2417864aa03a0dcdf17043@ec2-54-246-84-100.eu-west-1.compute.amazonaws.com:5432/d9kv8uh670d48o'


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
