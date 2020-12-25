from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(25), unique=True, nullable=False)
    hashed_pswd = db.Column(db.String(), nullable=False)

class History(db.Model):
    __tablename__ = "History"
    id = db.Column(db.Integer, primary_key=True)
    enc_username = db.Column(db.String(25))
    enc_email = db.Column(db.String(10000))
    enc_passwd = db.Column(db.String(20),nullable=False)
