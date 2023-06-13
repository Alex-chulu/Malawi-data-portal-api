"""_summary_
This is a district file that contains information about the district
The district file contains the following:
    - Import the Flask class and other modules
    - Flask app
    - Blueprints
    - Districts dictionary

    Returns:
        _type_: _description_
"""
from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

districts_bp = Blueprint('districts', __name__)
api = Api(districts_bp)


# Create a dictionary of districts and thier associated data
districts = [
        {
            "id": 0,
            "name": "Lilongwe",
            "population": 2000000,
            "hospitals": [
                {
                    "name": "Kamuzu Central Hospital",
                    "beds": 1000,
                    "doctors": 100,
                    "nurses": 200
                },
                {
                    "name": "Bwaila Hospital",
                    "beds": 500,
                    "doctors": 50,
                    "nurses": 100
                }
            ],
            "schools": [
                {
                    "id": 0,
                    "name": "Lilongwe Girls Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "id": 1,
                    "name": "Kamuzu Academy",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "id": 0,
                    "name": "Kabudula",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "id": 1,
                    "name": "Malingunde",
                    "population": 20000,
                    "males": 6000,
                    "females": 10000,
                    "children": 4000,
                }
            ]
        },
        {
            "id": 1,
            "name": "Blantyre",
            "population": 1500000,
            "hospitals": [
                {
                    "name": "Queen Elizabeth Central Hospital",
                    "beds": 1000,
                    "doctors": 100,
                    "nurses": 200
                },
                {
                    "name": "Mlambe Hospital",
                    "beds": 500,
                    "doctors": 50,
                    "nurses": 100
                }
            ],
            "schools": [
                {
                    "id": 0,
                    "name": "Blantyre Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "id": 1,
                    "name": "Chichiri Secondary School",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "id": 0,
                    "name": "Chirimba",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "id": 1,
                    "name": "Namiwawa",
                    "males": 6000,
                    "females": 6000,
                    "children": 4000,
                }
            ]
        }
    ]  # Replace with actual data


# Define the routes the districts blueprint will be handling
# This class will be used to get all districts
class Districts(Resource):
    def get(self):
        return jsonify(districts)
    
    # Create a method POST to add new district
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='District id is required')
        parser.add_argument('name', type=str, required=True, help='District name is required')
        parser.add_argument('population', type=int, required=True, help='District population is required')
        parser.add_argument('hospitals', type=list, required=True, help='District hospitals are required')
        parser.add_argument('schools', type=list, required=True, help='District schools are required')
        parser.add_argument('villages', type=list, required=True, help='District villages are required')
        params = parser.parse_args()
        
        for district in districts:
            if id == district['id']:
                return jsonify({'message': 'District with id ' +id+ ' already exists'})
            
        district = {
            'id': params['id'],
            'name': params['name'],
            'population': params['population'],
            'hospitals': params['hospitals'],
            'schools': params['schools'],
            'villages': params['villages']
        }
        
        districts.append(district)
        return jsonify({'District added successfully': district, 'status': 201})


# This route will be used to get a particular district
class District(Resource):
    def get(self, id):
        # filter the districts by id
        district = [district for district in districts if district['id'] == id]
        if district:
            return jsonify({'district': district})
        return jsonify({'Message': 'Invalid district id'})
    
    # Create a PUT method to update a district based on the id provided
    def put(self, id):
        # Update the district with new data based on the given id
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str)
        parser.add_argument('population', type=int)
        parser.add_argument('hospitals', type=list)
        parser.add_argument('schools', type=list)
        parser.add_argument('villages', type=list)
        params = parser.parse_args()
        
        for district in districts:
            if id == district['id']:
                district['id'] = params['id'] if params['id'] is not None else district['id']
                district['name'] = params['name'] if params['name'] is not None else district['name']
                district['population'] = params['population'] if params['population'] is not None else district['population']
                district['hospitals'] = params['hospitals'] if params['hospitals'] is not None else district['hospitals']
                district['schools'] = params['schools'] if params['schools'] is not None else district['schools']
                district['villages'] = params['villages'] if params['villages'] is not None else district['villages']
                return jsonify({'District updated successfully': district})
            
        return jsonify({'Message': 'District not found'})
    
    # Create a DELETE method to delete a district based on the id provided
    def delete(self, id):
        # Delete the district with the given id
        for district in districts:
            if id == district['id']:
                districts.remove(district)
                return jsonify({'Message': 'District deleted successfully'})
            
        return jsonify({'Message': 'District not found'})

# Register resources to the api service
api.add_resource(Districts, '/districts')
api.add_resource(District, '/districts/<int:id>')