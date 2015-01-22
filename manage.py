import os,sys
from flask.ext.script import Manager, Shell

sys.path.insert(0,os.path.abspath('.'))	#add current directory path to system path

from flask_login_demo.app import create_app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
