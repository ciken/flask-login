from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.bcrypt import Bcrypt
from flask.ext.bootstrap import Bootstrap

from .FlaskConfig import configSetting

bootstrap = Bootstrap()
login_manager = LoginManager()
db = MongoEngine() # connect MongoEngine with Flask App
flask_bcrypt = Bcrypt()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(configSetting[config_name])

	login_manager.init_app(app)
	db.init_app(app)
	bootstrap.init_app(app)
	app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine

	register_routes(app)

	return app

def register_routes(app):
	import auth.views
	import flask_login_demo.views

	app.register_blueprint(auth.views.bp, url_prefix='')
	app.register_blueprint(flask_login_demo.views.bp, url_prefix='')

