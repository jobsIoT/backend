from sqlalchemy.ext.declarative import declarative_base
from src.db import db
from src.to_json import OutputMixin

Base = declarative_base()


class User(OutputMixin, db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    ispremium = db.Column(db.Boolean, nullable=False)
    serialnumber = db.Column(db.String, nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "<Book( email='{}', firstname='{}', lastname='{}', password='{}', ispremium='{}', serialnumber='{}', isadmin='{}')>" \
            .format(self.email, self.firstname, self.lastname, self.password, self.ispremium, self.serialnumber, self.isadmin)


class Cardiaque(OutputMixin, db.Model):
    __tablename__ = 'cardiaque'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    rythme = db.Column(db.Integer, primary_key=False)
    date = db.Column(db.Text, nullable=True)
    #rythme cardiaque enregistré
    def __repr__(self):
        return "{{'id' : '{}', 'email' : '{}', 'rythme' : '{}', 'date' : '{}'}}" \
            .format(self.id, self.email, self.rythme, self.date)

class Journeys(OutputMixin, db.Model):
    __tablename__ = 'journeys'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    time = db.Column(db.Integer, primary_key=False)
    date = db.Column(db.Text, nullable=False)
    sleepingtime = db.Column(db.Integer, primary_key=False)
    alarm = db.Column(db.Integer, primary_key=False)
    destination = db.Column(db.Text, nullable=False)
    #voyage enregistré
    def __repr__(self):
        return "{{'id' : '{}', 'email' : '{}', 'time' : '{}', 'date' : '{}', 'sleepingtime' : '{}', 'alarm' : '{}', 'destination' : '{}'}}" \
            .format(self.id, self.email, self.time, self.date, self.sleepingtime, self.alarm, self.destination)