import os


def create_db_url(user, pw, url, db):
    return f"postgresql://{user}:{pw}@{url}/{db}"


class ConfDev(object):
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_URL = 'localhost'
    POSTGRES_DB = 'flaskdb'
    DATABASE_DEV_URL = create_db_url(POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB)
    SECRET_KEY = 'dev_key'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASE_DEV_URL
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfTest(object):
    POSTGRES_USER = os.environ.get("TESTING_POSTGRES_USER")
    POSTGRES_PW = os.environ.get("TESTING_POSTGRES_PW")
    POSTGRES_URL = os.environ.get("TESTING_POSTGRES_URL")
    POSTGRES_DB = os.environ.get("TESTING_POSTGRES_DB")
    DATABASE_TEST_URL = create_db_url(POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB)
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASE_TEST_URL
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfProd(object):
    DATABASE_PROD_URL = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = DATABASE_PROD_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
