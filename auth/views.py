# index view function suppressed for brevity
from flask_login_demo.app import login_manager, flask_bcrypt
from flask import render_template, Blueprint, request, url_for
from flask.ext.login import login_user, logout_user, current_app, current_user, login_required, flash, redirect
from .dbclass import User
from . import forms

bp = Blueprint('auth', __name__)

@bp.route("/register/", methods = ['GET', 'POST'])
def register():
	registerForm = forms.SignupForm()
	if registerForm.validate_on_submit():
		password_hash = flask_bcrypt.generate_password_hash(registerForm.password.data)
		user = User(user_username = registerForm.username.data, user_password = password_hash, user_email = registerForm.email.data)
		try:
			user.save()
			return "register success!"
		except Exception as e:
			return str(e)
	return render_template('auth/register.jinja', form = registerForm)

@bp.route("/login/", methods = ['GET', 'POST'])
def login():
	loginForm = forms.LoginForm()
	if loginForm.validate_on_submit():
		username = loginForm.username.data
		userObj = User()
		user = userObj.get_by_username_w_password(username)
		if user and flask_bcrypt.check_password_hash(user.user_password, request.form['password']) and user.is_active():
			remember = request.form.get("remember", "no") == "yes"
			if login_user(user, remember=remember):
				return redirect(request.args.get('next') or '/')
			else:
				return "unable to log you in"
	return render_template('auth/login.jinja', form = loginForm)

@bp.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect('/')

@login_manager.user_loader
def load_user(id):
	if id is None:
		redirect('/login/')
	user = User()
	user.get_by_id(id)
	if user.is_active():
		return user
	else:
		return None