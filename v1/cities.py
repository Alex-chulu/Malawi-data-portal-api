from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

cities_bp = Blueprint('cities', __name__)
api = Api(cities_bp)

cities = [
    {"id": 0, "name": "Lilongwe", "population": 989748, "region": "Central", "latitude": "-13.983333", "longitude": "33.783333"},
    {"id": 1, "name": "Blantyre", "population": 789498, "region": "Southern", "latitude": "-15.783333", "longitude": "35.000000"},
    {"id": 2, "name": "Mzuzu", "population": 189748, "region": "Northern", "latitude": "-11.466667", "longitude": "34.016667"}
]


# Create a class that inherits from Resource and return the data as JSON
# The class will return all cities availeble in the list
class Cities(Resource):
    def get(self):
        return jsonify({'cities': cities})
    
    # Create a POST method to add new entries to the list
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='City id is required')
        parser.add_argument('name', type=str, required=True, help='City name is required')
        parser.add_argument('population', type=int, required=True, help='City population is required')
        parser.add_argument('region', type=str)
        parser.add_argument('latitude', type=str)
        parser.add_argument('longitude', type=str)
        params = parser.parse_args()
        
        for city in cities:
            if id == city['id']:
                return jsonify({'message': 'City with id ' +id+ ' already exists'})
            
        city = {
            'id': params['id'],
            'name': params['name'],
            'population': params['population'],
            'region': params['region'],
            'latitude': params['latitude'],
            'longitude': params['longitude']
        }
        
        cities.append(city)
        return jsonify({'City added successfully': city, 'status': 201})
    

# Create a class that inherits from Resource and return the data as JSON
# The class will return a single city based on the id provided
# The class will also update and delete a city based on the id provided
class City(Resource):
    def get(self, id):
        city = [city for city in cities if city['id'] == id]
        if city:
            return jsonify({'city': city})
        return jsonify({'message': 'City not found'})
    
    # Create a PUT method to update a city based on the id provided
    def put(self, id):
        # Update the city with new data based on the given id
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('population', type=int)
        parser.add_argument('region', type=str)
        parser.add_argument('latitude', type=str)
        parser.add_argument('longitude', type=str)
        params = parser.parse_args()
        
        city = [city for city in cities if city['id'] == id]
        if not city:
            return jsonify({'message': 'City not found'})
        else:
            city = cities[id]
            city['name'] = params['name'] if params['name'] is not None else city['name']
            city['population'] = params['population'] if params['population'] is not None else city['population']
            city['region'] = params['region'] if params['region'] is not None else city['region']
            city['latitude'] = params['latitude'] if params['latitude'] is not None else city['latitude']
            city['longitude'] = params['longitude'] if params['longitude'] is not None else city['longitude']
            return city, 201
            
        
    # Create a DELETE method to delete a city based on the id provided
    def delete(self, id):
        city = [city for city in cities if city['id'] == id]
        if city:
            cities.remove(city[0])
            return jsonify({'message': 'City deleted successfully'})
        return jsonify({'message': 'City not found'})
    

# Add the resource to the api
api.add_resource(Cities, '/cities')
api.add_resource(City, '/cities/<int:id>')