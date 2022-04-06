from flask_restful import Resource
from common.models.user import UserModel

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

        return {"Users": results}