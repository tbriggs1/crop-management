from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tbriggs:example@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecret'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# TODO - Add library CORS(app)

jwt = JWT(app, authenticate, identity)

items = []

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



class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    # @jwt_required()
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        result = {"id": id, "firstname": user.firstname, "lastname": user.lastname}

        return {"user": result}

    def post(self, id):
        if request.json:
            data = request.get_json()
            new_user = UserModel(id=id, firstname=data['firstname'], lastname=data['lastname'])
            db.session.add(new_user)
            db.session.commit()

            return {"Message": f"Registration for {new_user.firstname} {new_user.lastname} has been created successfully"}

        return {"Error": "Unable to create user"}

    # @jwt_required()
    def delete(self):
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "user deleted"}

    # @jwt_required()
    def put(self, id):
        user = UserModel.query.get_or_404(id)
        data = request.get_json()
        user.firstname = data['firstname']
        user.lastname = data['lastname']
        db.session.add(user)
        db.session.commit()
        return {"message": "Successfully updated user details"}

class Users(Resource):
    def get(self):
        users = UserModel.query.all()
        results = [
            {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
            } for user in users
        ]

api.add_resource(User, '/user/<string:id>')
api.add_resource(Users, '/users')


if __name__ == "__main__":
    db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
