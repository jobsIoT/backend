from sqlalchemy.ext.declarative import declarative_base
from src.db import db
from src.to_json import OutputMixin

Base = declarative_base()


class User(OutputMixin, db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Book(name='{}', prenom='{}', mail={}, tel={})>" \
            .format(self.name, self.lastname, self.email, self.phone_nb,
                    self.password)


class Cardiaque(OutputMixin, db.Model):
    __tablename__ = 'cardiaque'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    rythme = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text, nullable=True)
    #rythme cardiaque enregistrer
    def __repr__(self):
        return "{{'id' : '{}', 'email' : '{}', 'rytme' : '{}', 'date' : '{}'}}" \
            .format(self.id, self.email, self.rythme, self.date)