from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
import os
from common.resources.users import Users
from common.resources.user_crud import User
from common.configuration.db import db
from common.resources.crop_crud import Crop
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://tbriggs:example@51.89.220.72/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecret"
db.init_app(app)

CORS(app)


jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, "/user")
api.add_resource(Users, "/profile")
api.add_resource(Crop, "/crop")


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
