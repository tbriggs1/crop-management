from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required
from common.models.user import UserModel
from common.configuration.db import db
from common.utils.token import Token
import uuid


class User(Resource):


    @jwt_required()
    def get(self):
        data = request.headers
        token = Token(data)
        user = UserModel.find_by_id(token.identity)

        return {'firstname': user.firstname,
                'password': user.password,
                'username': user.username
                }


    def post(self):
        if request.json:
            data = request.get_json()
            new_user = UserModel(
                id=str(uuid.uuid4()),
                username=data["username"],
                firstname=data["firstname"],
                lastname=data["lastname"],
                email=data["email"],
                password=data["password"],
            )

            if UserModel.find_by_username(data['username']) and UserModel.find_by_email(data['email']):
                return {
                    "Message": f"Username {data['username']} and Email {data['email']} already exists"
                }, 409

            if UserModel.find_by_username(data['username']):
                return {
                    "Message": f"Username {data['username']} already exists"
                }, 409

            if UserModel.find_by_email(data['email']):
                return {
                        "Message": f"Email {data['email']} already exists"
                       }, 409

            db.session.add(new_user)
            db.session.commit()

            return {
                "Message": f"Registration for {new_user.firstname} {new_user.lastname} has been created successfully"
            }

        return {"Error": "Unable to create user"}

    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "user deleted"}

    def put(self, id):
        user = UserModel.query.get_or_404(id)
        data = request.get_json()
        user.username = data["username"]
        user.firstname = data["firstname"]
        user.lastname = data["lastname"]
        user.email = data["email"]
        user.password = data["password"]
        db.session.add(user)
        db.session.commit()
        return {"message": "Successfully updated user details"}
