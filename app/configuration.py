class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URI = ''
	BOOTSTRAP_FONTAWESOME = True
	SECRET_KEY = 'SECRETKEY'
	CSRF_ENABLED = True


class ProductionConfig(Config):
	DATABASE_URI = ''


class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True

