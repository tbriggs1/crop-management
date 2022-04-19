from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required
from common.models.crop import CropModel
from common.configuration.db import db
import uuid


class Crop(Resource):

    # TODO - Add for login @jwt_required()
    def get(self):
        data = request.get_json()
        crops = CropModel.query.filter_by(username=data["username"]).first()
        result = {"crop": crops.name, "planted": crops.time_planted}

        return {"user": result}

    def post(self):
        if request.json:
            data = request.get_json()
            new_crop = CropModel(
                id=str(uuid.uuid4()),
                name=data["name"],
                time_planted=data["time_planted"],
                username=data["username"],
            )
            db.session.add(new_crop)
            db.session.commit()

            return {"Message": f"Crop {new_crop.name} has been created successfully"}

        return {"Error": "Unable to create user"}

    def delete(self, id):
        crop = CropModel.query.get_or_404(id)
        db.session.delete(crop)
        db.session.commit()
        return {"message": "crop deleted"}

    def put(self, id):
        crop = CropModel.query.get_or_404(id)
        data = request.get_json()
        crop.name = data["name"]
        crop.time_planted = data["time_planted"]
        crop.username = data["username"]

        db.session.add(crop)
        db.session.commit()
        return {"message": "Successfully updated crop details"}
