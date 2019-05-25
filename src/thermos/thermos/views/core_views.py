# Third party imports
from flask import url_for, render_template, redirect, flash, current_app as app
from sqlalchemy import func

# Local application imports
from ..viewmodels.add_form import BookmarkForm
from .. import db
from ..models.bookmark import Bookmark
from ..models.user import User
from ..viewmodels.core_view_models import logged_in_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title_bar = 'Welcome', new_bookmarks=Bookmark.newest(2))


@app.route('/add', methods=['GET', 'POST'])
def add_url():
    add_form = BookmarkForm()
    # if request.method == 'POST':
    if add_form.validate_on_submit():
        # url = request.form['url']
        url = add_form.url.data
        description = add_form.description.data
        b = Bookmark(User=logged_in_user(), url=url, description=description)
        db.session.add(b)
        db.session.commit()
        # store_bookmark(url, description)
        app.logger.debug('stored url: ' + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=add_form, title_bar='Add a URL')


@app.route('/user/<username>')
def user_bookmarks(username):
    user = User.query.filter(func.lower(User.username) == username.lower()).first_or_404()
    bookmarks = Bookmark.query.filter_by(user_id=user.id).all()
    return render_template('user.html', title_bar = 'User Bookmarks', user=user, bookmarks=bookmarks)

