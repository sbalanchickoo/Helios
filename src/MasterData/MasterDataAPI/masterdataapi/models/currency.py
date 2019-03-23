from run import db


class Currency(db.Model):
    __tablename__ = 'Currency'
    id = db.Column(db.Integer, primary_key = True)
    currcode = db.Column(db.String(3))
    currency = db.Column(db.String(128))

    def __repr__(self):
        return 'Currency Code: {}; Currency: {}'.format(self.currcode, self.currency)

    @property
    def serialize(self):
        return {
            'currcode': self.currcode,
            'currency': self.currency
        }

