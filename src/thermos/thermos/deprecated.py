# Fake login
def logged_in_user():
    return User.query.filter_by(username='Shri').first()


def store_bookmark(url, description):
    bookmarks.append({
        'url': url,
        'description': description,
        'user': 'Srikant',
        'date_added': datetime.utcnow()
    })


bookmarks = []


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bookmark: bookmark['date_added'], reverse=True)[:num]


