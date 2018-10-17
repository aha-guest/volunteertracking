from flask import Blueprint
from volunteermatching import db, app
from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = 'login'

bp_auth = Blueprint('auth', __name__)

from .models import Role, User
#from . import views, forms
