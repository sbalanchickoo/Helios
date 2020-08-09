from flask import render_template
from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from ..models.user import User
from ..models.blood_pressure_log import BloodPressureLog
from ..viewmodels.blood_pressure_log_form import BloodPressureLogForm
from ..viewmodels.login_form import LoginForm
from ..viewmodels.signup_form import SignupForm
from ..viewmodels.login_manager import load_user
from .. import db


# <name of blueprint to be registered> = Blueprint('<friendly name to be used in URLs>', __name__)
core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/')
@core_blueprint.route('/index')
def index():
    return render_template('index.html')


@core_blueprint.route('/bloodpressure', methods=['GET', 'POST'])
@login_required
def log_blood_pressure():
    local_form = BloodPressureLogForm()
    recent = BloodPressureLog.newest(5)
    if request.method == 'POST' and request.form.post['action'] == 'Download':
        if local_form.validate_on_submit():
            blood_pressure_entry = BloodPressureLog(
                systolic=int(local_form.systolic.data),
                diastolic=int(local_form.diastolic.data),
                heart_rate=int(local_form.heart_rate.data),
                date=local_form.date.data,
                user=current_user,
                notes=local_form.notes.data,
            )
        db.session.add(blood_pressure_entry)
        db.session.commit()
        flash("Blood pressure entry added!")
        return redirect(url_for('core.log_blood_pressure'))
    return render_template('blood_pressure_log.html'
                           , form=local_form
                           , title_bar='Add blood pressure details'
                           , recent=recent)


@core_blueprint.route('/login', methods=['GET', 'POST'])
def sign_in():
    local_form = LoginForm()
    # if request.method == 'POST':
    if local_form.validate_on_submit():
        username = local_form.username.data
        password = local_form.password.data
        cur_user = User.get_by_username(username)
        if cur_user is not None and cur_user.check_password(password):
            login_user(cur_user, local_form.remember_me.data)
            flash("User '{}' logged in successfully!".format(username))
            return redirect(request.args.get('next') or url_for('core.index'))
        else:
            flash("Incorrect username or password")
    return render_template('login.html', form=local_form, title_bar='User Login')


@core_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    local_form = SignupForm()
    # if request.method == 'POST':
    if local_form.validate_on_submit():
        user_entry = User(
            email=local_form.email.data,
            username = local_form.username.data,
            password = local_form.password.data,
        )
        db.session.add(user_entry)
        db.session.commit()
        flash("Welcome! '{}'! Please login.".format(local_form.username.data))
        return redirect(url_for('core.sign_in'))
    return render_template('signup.html', form=local_form, title_bar='User Signup')


@core_blueprint.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('core.index'))