from flask import Blueprint, jsonify
from flask import Flask, request, jsonify
from flask_restful import Api, Resource # used for REST API building


from model.model_geoguesser import *

geoguesser_api = Blueprint('geoguesser_api', __name__, url_prefix='/api/geoguesser')

api = Api(geoguesser_api)

class GeoguesserAPI:
    class _ReadRandom(Resource):
        def get(self):
            country_info = get_random_country()
            if country_info:
                return jsonify(get_random_country())
            return jsonify({"error": "get_random_country() failed, "}), 404
        

    api.add_resource(_ReadRandom, '/random')

