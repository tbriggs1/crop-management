from flask_restful import Resource
from common.models.user import UserModel
from flask_jwt import jwt_required

class Users(Resource):
    @jwt_required()
    def get(self):
        response_body = {
            "name": "Nagato",
            "about": "Hello! I'm a full stack developer that loves python and javascript"
        }

        return response_body
