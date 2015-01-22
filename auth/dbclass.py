from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import (LoginManager, current_user, login_required,
							login_user, logout_user, UserMixin, AnonymousUserMixin,
							confirm_login, fresh_login_required)
from . import models

class User(UserMixin):
	def __init__(self, user_username=None, user_password=None, user_email=None, user_isactive=True, id=None):
		self.user_email = user_email
		self.user_username = user_username
		self.user_password = user_password
		self.user_isactive = user_isactive
		self.id = None

	def save(self):
		newUser = models.User(user_username=self.user_username, user_password=self.user_password, user_email=self.user_email, user_isactive=self.user_isactive)
		newUser.save()
		self.id = newUser.id
		return self.id

	def get_by_username_w_password(self, user_username):
		try:
			dbUser = models.User.objects.get(user_username = user_username)
			if dbUser:
				self.user_username = dbUser.user_username
				self.user_password = dbUser.user_password
				self.user_isactive = dbUser.user_isactive
				self.id = dbUser.id
				return self
			else:
				return None
		except:
			return None

	def get_by_id(self, id):
		dbUser = models.User.objects.with_id(id)
		if dbUser:
			self.user_username = dbUser.user_username
			self.user_isactive = dbUser.user_isactive
			self.id = dbUser.id
		return self

	def is_active(self):
		return True

class Anonymous(AnonymousUserMixin):
	name = "Anonymous"