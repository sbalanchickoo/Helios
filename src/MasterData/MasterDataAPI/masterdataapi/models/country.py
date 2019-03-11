from config import db


class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column(db.Integer, primary_key = True)
    currencycode = db.Column('currcode', db.String(3))
    countryname = db.Column('country', db.String(128))

    def __repr__(self):
        return 'Currency Code: {}; Country: {}'.format(self.currencycode, self.countryname)

    @property
    def serialize(self):
        return {
            'currency_code': self.currencycode,
            'country_name': self.countryname
        }
