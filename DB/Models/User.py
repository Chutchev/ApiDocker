from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(12), index=True, unique=True)
    city = db.Column(db.String(20), index=True)
    country = db.Column(db.String(64), index=True)
    address = db.Column(db.String(256), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f"User id: <{self.id}>"

    def to_json(self):
        return {
                   "id": self.id,
                   "email": self.email,
                   "first_name": self.first_name,
                   "last_name": self.last_name,
                   "phone": self.phone,
                   "country": self.country,
                   "city": self.city,
                   "address": self.address
               }

