import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    BUCKETLISTS_PER_PAGE = 20
    MIN_BUCKETLISTS_PER_REQUEST = 1
    MAX_BUCKETLISTS_PER_REQUEST = 100
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    BUCKETLISTS_PER_PAGE = 2
    MAX_BUCKETLISTS_PER_REQUEST = 10
    SQLALCHEMY_DATABASE_URI = "postgresql://@localhost/buckets"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://@localhost/test_db"
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}