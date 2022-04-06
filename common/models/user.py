from common.configuration.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname =lastname

    def __repr__(self):
        return f"<User {self.firstname}>"
