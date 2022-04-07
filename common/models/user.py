from common.configuration.db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String())
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, firstname, lastname, email, password ):
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