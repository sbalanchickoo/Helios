from datetime import datetime
from thermos import db
from sqlalchemy import desc


class Bookmark(db.Model):
    __tablename__ = 'Bookmark'
    id = db.Column('id', db.Integer, primary_key=True)
    url = db.Column('url', db.Text, nullable=False)
    date = db.Column(db.DateTime, default= datetime.utcnow)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)

    def __repr__(self):
        return "<Bookmark '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'date': self.date,
            'description': self.description
        }
