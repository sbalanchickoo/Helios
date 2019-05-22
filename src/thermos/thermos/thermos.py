import os
from flask import Flask, url_for, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from logging import DEBUG
from addform import BookmarkForm
from config import Config
from run import create_app

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.logger.setLevel(DEBUG)
# app.config['SECRET_KEY'] = "b'|\xec\x08\x8b<\x93m\x11\x03YP\x8a\xcc]\xf5\xc1k]\xf5\xa4""\xd0[\x91'"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
# app.config.from_object(Config)
# db = SQLAlchemy(app)
app = create_app()

bookmarks = []


def store_bookmark(url, description):
    bookmarks.append({
        'url': url,
        'description': description,
        'user': 'Srikant',
        'date_added': datetime.utcnow()
    })


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bookmark: bookmark['date_added'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title_bar = 'Welcome', new_bookmarks=new_bookmarks(2))


@app.route('/add', methods=['GET', 'POST'])
def add_url():
    add_form = BookmarkForm()
    # if request.method == 'POST':
    if add_form.validate_on_submit():
        # url = request.form['url']
        url = add_form.url.data
        description = add_form.description.data
        store_bookmark(url, description)
        app.logger.debug('stored url: ' + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=add_form, title_bar='Add a URL')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
