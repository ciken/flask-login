from flask_login_demo.app import db
class User(db.Document):
    user_username = db.StringField(required=True, unique=True, max_length=16)
    user_password = db.StringField(required=True, max_length=60)
    user_email = db.EmailField(required=True, unique=True)
    user_isactive = db.BooleanField(default=False)