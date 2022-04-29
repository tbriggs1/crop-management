from common.configuration.db import db

from sqlalchemy.dialects.postgresql import UUID


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String())
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, id, username, firstname, lastname, email, password):
        self.id = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
