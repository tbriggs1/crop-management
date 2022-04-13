from common.configuration.db import db


class CropModel(db.Model):
    __tablename__ = "crops"

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    time_planted = db.Column(db.String())
    username = db.Column(db.String())

    def __init__(self, id, name, time_planted, username):
        self.id = id
        self.name = name
        self.time_planted = time_planted
        self.username = username

    def __repr__(self):
        return f"<User {self.username}>"
