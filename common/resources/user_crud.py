from flask_restful import Resource
from flask import request
from common.models.user import UserModel
from common.configuration.db import db

class User(Resource):

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