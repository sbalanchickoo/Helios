# Notes

## Installation

1. Python
2. pip
3. pip install virtualenv
4. pip install virtualenvwrapper-win
5. python -m venv "environment name"
6. scripts\activate
7. pip install flask

## Points

- If its a package, you need __init__.py (empty is fine)
- Boilerplate code can be downloaded from initializr.com (responsive option is fine, you can choose options)
  - Move html files to templates folder
  - Move other folders (css etc.) as they are into the static folder
- url_for(view)
- url_for('static', filename='relative path')
- app.errorhandler(404)
  - render_template('404.html'), 404
- Resources
  - jinja.pocoo.org
  - initializr.com
  - flask.pocoo.org/docs/quickstart/#url-building/
- request object
  - files
  - query string
  - form
  - cookies
  - headers
