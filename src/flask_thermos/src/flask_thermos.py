from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from .bookmarkform import BookmarkForm

from logging import DEBUG

# Main application constructor
app = Flask(__name__)
app.config["SECRET KET"] = "b'\xc7s)s\x8cv\x80\xc9\xf3\xf5\xf1\x97}\xc3\xe3\xf5\x99\xb2\xa8\xefi9\xa2\xb4'"
app.secret_key = "b'\xc7s)s\x8cv\x80\xc9\xf3\xf5\xf1\x97}\xc3\xe3\xf5\x99\xb2\xa8\xefi9\xa2\xb4'"
# app.logger.setLevel(DEBUG)
bookmarks = []


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


def add_bookmark(url):
    bookmarks.append(dict(
            url=url,
            user="sb",
            date=datetime.utcnow()
        )
    )


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = BookmarkForm()
        if form.validate_on_submit():
            url = form.url.data
            # request.form['url']
            add_bookmark(url)
        # app.logger.debug('url added: ', url)
        flash("Stored Bookmark: {}".format(url))
        return redirect(url_for("index"))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=False)