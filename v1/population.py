from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

population_bp = Blueprint('population', __name__)
api = Api(population_bp)


total_population = 19129952
region_population = [
            {"id": 0, "region": "Northern", "population": 3593479},
            {"id": 1, "region": "Central", "population": 12173448},
            {"id": 2, "region": "Southern", "population": 3433045}
        ]

# Create a class that inherits from Resource and return the data as JSON
# This class returns all population information 
class PopulationList(Resource):
    def get(self):
        
        response = {
            "total_population": total_population,
            "region_population": region_population
        }
        return jsonify({"Total National Population": total_population},
        {"Population by region": region_population})
    
class Population(Resource):
    def get(self, id):
        pop = [pop for pop in region_population if pop['id'] == id]
        if pop:
            return jsonify({'Population': pop})
        return jsonify({'Message': 'Population not found'})

# Register the resource and its endpoints
api.add_resource(PopulationList, '/population')
api.add_resource(Population, '/population/<int:id>')