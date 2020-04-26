from flask import render_template
from flask import Blueprint, flash, redirect, url_for, request
from ..viewmodels import \
    blood_pressure_log_form\
    , metrics_log_form\
    , exercise_log_form\
    , exercise_metadata_form\
    , body_part_metadata_form\
    , signup_form\
    , login_form as lg_form
from ..viewmodels.signup_form import SignupForm
from ..models import \
    metrics_log\
    , user\
    , blood_pressure_log\
    , body_part_metadata\
    , exercise_metadata\
    , exercise_log
from .. import db
from decimal import Decimal
from ..config import Config
from datetime import datetime
from flask_login import login_required, login_user, logout_user, current_user
from ..viewmodels.login_manager import load_user

# <name of blueprint to be registered> = Blueprint('<friendly name to be used in URLs>', __name__)
core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/')
@core_blueprint.route('/index')
def index():
    return render_template('index.html')


@core_blueprint.route('/bloodpressure', methods=['GET', 'POST'])
@login_required
def log_blood_pressure():
    bp_form = blood_pressure_log_form.BloodPressureForm()
    recent = blood_pressure_log.BloodPressure.newest(5)
    if request.method == 'POST':
        if bp_form.validate_on_submit():
            blood_pressure_entry = blood_pressure_log.BloodPressure(
                systolic=int(bp_form.systolic.data),
                diastolic=int(bp_form.diastolic.data),
                date=bp_form.date.data,
                user=current_user,
                notes=bp_form.notes.data,
            )
            db.session.add(blood_pressure_entry)
            db.session.commit()
            flash("Blood pressure entry added!")
            return redirect(url_for('core.log_blood_pressure'))
    else:
        entries = [entry for entry in recent]
        if len(entries) > 0:
            recent_entry = max(entries, key=lambda x: x.date)
        else:
            recent_entry = blood_pressure_log.BloodPressure(
                systolic=0,
                diastolic=0,
                date=datetime.utcnow(),
                user=current_user
            )
        bp_form.systolic.data = recent_entry.systolic
        bp_form.diastolic.data = recent_entry.diastolic
        bp_form.date.data = recent_entry.date
        return render_template('blood_pressure_log.html', form=bp_form
                               , title_bar='Add blood pressure details'
                               , recent=recent)
    return render_template('metrics_log.html', form=blood_pressure_log_form.BloodPressureForm()
                           , title_bar='Add blood pressure details')


@core_blueprint.route('/metrics', methods=['GET', 'POST'])
@login_required
def log_metrics():
    local_form = metrics_log_form.MetricsLogForm()
    recent = metrics_log.MetricsLog.newest(5)
    if request.method == 'POST':
        if local_form.validate_on_submit():
            new_metrics_log = metrics_log.MetricsLog(
                body_weight=Decimal(local_form.body_weight.data),
                body_fat_percent = Decimal(local_form.body_fat_percent.data),
                bmi=Decimal(local_form.bmi.data),
                date=local_form.date.data,
                user=current_user,
                notes=local_form.notes.data,
            )
            db.session.add(new_metrics_log)
            db.session.commit()
            flash("Metrics added!")
            return redirect(url_for('core.log_metrics'))
    else:
        entries = [entry for entry in recent]
        if len(entries) > 0:
            recent_entry = max(entries, key=lambda x: x.date)
        else:
            recent_entry = metrics_log.MetricsLog(
                body_weight=0,
                body_fat_percent=0,
                bmi=0,
                date=datetime.utcnow(),
                user=current_user
            )
        local_form.body_weight.data = recent_entry.body_weight
        local_form.body_fat_percent.data = recent_entry.body_fat_percent
        local_form.bmi.data = recent_entry.bmi
        local_form.date.data = recent_entry.date
        return render_template('metrics_log.html', form=local_form
                               , title_bar='Add weight details'
                               , recent=recent)
    return render_template('metrics_log.html', form=metrics_log_form.MetricsLogForm()
                           , title_bar='Add weight details'
                           , recent=recent)


@core_blueprint.route('/exercise', methods=['GET', 'POST'])
@login_required
def log_exercise():
    local_form = exercise_log_form()
    recent = metrics_log.MetricsLog.newest(5)
    if request.method == 'POST':
        if local_form.validate_on_submit():
            new_metrics_log = metrics_log.MetricsLog(
                body_weight=Decimal(local_form.body_weight.data),
                body_fat_percent = Decimal(local_form.body_fat_percent.data),
                bmi=Decimal(local_form.bmi.data),
                date=local_form.date.data,
                user=current_user,
                notes=local_form.notes.data,
            )
            db.session.add(new_metrics_log)
            db.session.commit()
            flash("Metrics added!")
            return redirect(url_for('core.log_metrics'))
    else:
        entries = [entry for entry in recent]
        if len(entries) > 0:
            recent_entry = max(entries, key=lambda x: x.date)
        else:
            recent_entry = metrics_log.MetricsLog(
                body_weight=0,
                body_fat_percent=0,
                bmi=0,
                date=datetime.utcnow(),
                user=current_user
            )
        local_form.body_weight.data = recent_entry.body_weight
        local_form.body_fat_percent.data = recent_entry.body_fat_percent
        local_form.bmi.data = recent_entry.bmi
        local_form.date.data = recent_entry.date
        return render_template('metrics_log.html', form=local_form
                               , title_bar='Add weight details'
                               , recent=recent)
    return render_template('metrics_log.html', form=metrics_log_form.MetricsLogForm()
                           , title_bar='Add weight details'
                           , recent=recent)


@core_blueprint.route('/manage', methods=['GET', 'POST'])
@login_required
def log_metrics():
    local_form = metrics_log_form.MetricsLogForm()
    recent = metrics_log.MetricsLog.newest(5)
    if request.method == 'POST':
        if local_form.validate_on_submit():
            new_metrics_log = metrics_log.MetricsLog(
                body_weight=Decimal(local_form.body_weight.data),
                body_fat_percent = Decimal(local_form.body_fat_percent.data),
                bmi=Decimal(local_form.bmi.data),
                date=local_form.date.data,
                user=current_user,
                notes=local_form.notes.data,
            )
            db.session.add(new_metrics_log)
            db.session.commit()
            flash("Metrics added!")
            return redirect(url_for('core.log_metrics'))
    else:
        entries = [entry for entry in recent]
        if len(entries) > 0:
            recent_entry = max(entries, key=lambda x: x.date)
        else:
            recent_entry = metrics_log.MetricsLog(
                body_weight=0,
                body_fat_percent=0,
                bmi=0,
                date=datetime.utcnow(),
                user=current_user
            )
        local_form.body_weight.data = recent_entry.body_weight
        local_form.body_fat_percent.data = recent_entry.body_fat_percent
        local_form.bmi.data = recent_entry.bmi
        local_form.date.data = recent_entry.date
        return render_template('metrics_log.html', form=local_form
                               , title_bar='Add weight details'
                               , recent=recent)
    return render_template('metrics_log.html', form=metrics_log_form.MetricsLogForm()
                           , title_bar='Add weight details'
                           , recent=recent)


@core_blueprint.route('/login', methods=['GET', 'POST'])
def sign_in():
    login_form = lg_form.LoginForm()
    # if request.method == 'POST':
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        cur_user = user.User.get_by_username(username)
        if cur_user is not None and cur_user.check_password(password):
            login_user(cur_user, login_form.remember_me.data)
            flash("User '{}' logged in successfully!".format(username))
            return redirect(request.args.get('next') or url_for('core.index'))
        else:
            flash("Incorrect username or password")
    return render_template('login.html', form=login_form, title_bar='User Login')


@core_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    # if request.method == 'POST':
    if signup_form.validate_on_submit():
        user_entry = user.User(
            email=signup_form.email.data,
            username = signup_form.username.data,
            password = signup_form.password.data,
        )
        db.session.add(user_entry)
        db.session.commit()
        flash("Welcome! '{}'! Please login.".format(signup_form.username.data))
        return redirect(url_for('core.sign_in'))
    return render_template('signup.html', form=signup_form, title_bar='User Signup')


@core_blueprint.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('core.index'))