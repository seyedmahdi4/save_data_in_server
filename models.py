from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    enx_object = db.Column(db.String(500))
