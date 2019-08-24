# Standard library imports

# Third party imports
from flask import url_for, render_template, request, redirect, flash, current_app as app, abort
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import func

# Local application imports
from ..viewmodels.bookmark_form import BookmarkForm
from ..viewmodels.login_form import LoginForm
from ..viewmodels.signup_form import SignupForm
from .. import db, login_manager
from ..models.bookmark import Bookmark
from ..models.user import User
from ..viewmodels.core_view_models import load_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title_bar = 'Welcome', new_bookmarks=Bookmark.newest(2))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_url():
    add_form = BookmarkForm()
    # if request.method == 'POST':
    if add_form.validate_on_submit():
        # url = request.form['url']
        url = add_form.url.data
        description = add_form.description.data
        b = Bookmark(user=current_user, url=url, description=description)
        db.session.add(b)
        db.session.commit()
        # store_bookmark(url, description)
        app.logger.debug('stored url: ' + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('bookmark_form.html', form=add_form, operation='Add a URL')


@app.route('/edit/<int:bookmark_id>', methods=['GET', 'POST'])
@login_required
def edit_url(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    if current_user != bookmark.user:
        abort(403)
    edit_form = BookmarkForm(obj=bookmark)
    # if request.method == 'POST':
    if edit_form.validate_on_submit():
        edit_form.populate_obj(bookmark)
        db.session.commit()
        app.logger.debug('stored url: ' + bookmark.url)
        flash("Stored bookmark '{}'".format(bookmark.url))
        return redirect(url_for('index'))
    return render_template('bookmark_form.html', form=edit_form, operation='Edit a URL')


@app.route('/user/<username>')
@login_required
def user_bookmarks(username):
    user = User.get_by_username(username=username)

#    user = User.query.filter(func.lower(User.username) == username.lower()).first_or_404()
    bookmarks = Bookmark.query.filter_by(user_id=user.id).all()
    return render_template('user.html', title_bar = 'User Bookmarks', user=user, all_bookmarks=Bookmark.all())


@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    login_form = LoginForm()
    # if request.method == 'POST':
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.get_by_username(username)
        # user = User.query.filter(func.lower(username) == username.lower()).first()
        if user is not None and user.check_password(password):
            login_user(user, login_form.remember_me.data)
            flash("User '{}' logged in successfully!".format(username))
            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash("Incorrect username or password")
    return render_template('login.html', form=login_form, title_bar='User Login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    # if request.method == 'POST':
    if signup_form.validate_on_submit():
        user = User(
            email=signup_form.email.data,
            username = signup_form.username.data,
            password = signup_form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Welcome! '{}'! Please login.".format(signup_form.username.data))
        return redirect(url_for('sign_in'))
    return render_template('signup.html', form=signup_form, title_bar='User Signup')


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))