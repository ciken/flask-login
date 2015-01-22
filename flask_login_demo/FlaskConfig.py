import os
class baseConfig:
	CSRF_ENABLED = True,
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


class developmentConfig(baseConfig):
	DEBUG = True
	MONGODB_SETTINGS = {'HOST':'localhost' ,'DB': 'test'}

class testingConfig(baseConfig):
	TESTING = True
	MONGODB_SETTINGS = {'HOST':'localhost' ,'DB': 'test'}

class productionConfig(baseConfig):
	MONGODB_SETTINGS = {'HOST':'localhost' ,'DB': 'test'}

configSetting = {
	'development': developmentConfig,
    'testing': testingConfig,
    'production': productionConfig,

    'default': developmentConfig
}