from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

config_state = os.environ.get('CONFIG_MODE')

if config_state == 'DEV':
	app.config.from_object('configuration.DevelopmentConfig')
elif config_state == 'TEST':
	app.config.from_object('configuration.TestingConfig')
else:
	app.config.from_object('configuration.ProductionConfig')

bootstrap = Bootstrap(app)

from app import views, models
