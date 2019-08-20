import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'IamTheCreatorOfUniverse')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    #SQLALCHEMY_DATABASE_URI = 'postgresql://urs:pass@localhost:5432/sqlalchemy'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'games.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base



config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
