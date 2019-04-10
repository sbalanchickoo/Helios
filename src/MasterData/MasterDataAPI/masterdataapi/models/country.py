from run import db


class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column(db.Integer, primary_key = True)
    currency_code = db.Column('currcode', db.String(3))
    country_name = db.Column('country', db.String(128))

    def __repr__(self):
        return 'Currency Code: {}; Country: {}'.format(self.currency_code, self.country_name)

    @property
    def serialize(self):
        return {
            'id':self.id,
            'currency_code': self.currency_code,
            'country_name': self.country_name
        }

    @staticmethod
    def add_country(new_country):
        db.session.add(new_country)
        db.session.commit()
        return 1

    @staticmethod
    def update_country_name(old_name, new_name):
        Country.query.filter_by(country_name = old_name).update({'country_name':new_name})
        db.session.commit()
        return 1
