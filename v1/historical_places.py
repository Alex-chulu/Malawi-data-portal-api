from flask import Blueprint, jsonify 
from flask_restful import Resource, Api, reqparse

historical_places_bp = Blueprint('historical_places', __name__)
api = Api(historical_places_bp)

historical_places = [
        {
            "id": 0,
            "name": "Chongoni Rock Art Area",
            "description": "Chongoni Rock Art Area is a UNESCO World Heritage Site located in Central Malawi, Africa. It was first designated in 2006. The site contains the most concentrated cluster of rock art found in Central Africa. It is situated on a plateau overlooking the Malawi Rift Valley.",
            "district": "Dedza"
        },
        {
            "id": 1,
            "name": "Lake Malawi National Park",
            "description": "Lake Malawi National Park is a national park located in Malawi at the southern end of Lake Malawi. It is the only national park in Malawi that was created to protect fish and aquatic habitats. Despite this, Lake Malawi National Park includes a fair amount of land, including several small islands in Lake Malawi. The park is home to many hundreds of fish species, nearly all endemic.",
            "district": "Mangochi"
        },
        {
            "id": 2,
            "name": "Mua Mission",
            "description": "Mua Mission is a Catholic mission in Malawi, located in the village of Mua. It was founded in 1902 by the White Fathers. The mission is known for its woodcarvings and the Chamare Museum, which is located on the mission grounds. The museum is known for its collection of Gule Wamkulu masks, which are used in the Gule Wamkulu dance of the Chewa people.",
            "district": "Dedza"
        },
        {
            "id": 3,
            "name": "Livingstonia Mission",
            "description": "Livingstonia Mission is a mission station of the Church of Central Africa Presbyterian in northern Malawi, south of the town of Chitimba and close to the lake shore. It was founded by missionaries from the Free Church of Scotland in 1894 and named after the Scottish missionary and explorer David Livingstone. The mission was built on a high plateau, 900 metres above Lake Malawi, overlooking the Rift Valley and Nyika Plateau.",
            "district": "Rumphi"
        }
    ]

# Create class and method to access historical places
class HistoricalPlaces(Resource):
    def get(self):
        return jsonify(historical_places)
    
    
    # Create a POST method to add new entries to the list
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Historical place id is required')
        parser.add_argument('name', type=str, required=True, help='Historical place name is required')
        parser.add_argument('description', type=str, required=True, help='Historical place description is required')
        parser.add_argument('district', type=str, required=True, help='Historical place district is required')
        params = parser.parse_args()
        
        for historical_place in historical_places:
            if id == historical_place['id']:
                return jsonify({'message': 'Historical place with id ' +id+ ' already exists'})
            
        historical_place = {
            'id': params['id'],
            'name': params['name'],
            'description': params['description'],
            'district': params['district']
        }
        
        historical_places.append(historical_place)
        return jsonify({'Historical place added successfully': historical_place, 'status': 201})


# Create class and method to access historical places in a particular district
class HistoricalPlace(Resource):    
    # Create a GET method to get historical places based on the id provided
    def get(self, id):
        historical_place = [historical_place for historical_place in historical_places if historical_place['id'] == id]
        if historical_place:
            return jsonify({'historical_place': historical_place})
        return jsonify({'Message': 'Historical place not found'})
    
    
    # Create a PUT method to update a historical place based on the id provided
    def put(self, id):
        # Update the historical place with new data based on the given id
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('district', type=str)
        params = parser.parse_args()
        
        for historical_place in historical_places:
            if id == historical_place['id']:
                historical_place['id'] = params['id'] if params['id'] is not None else historical_place['id']
                historical_place['name'] = params['name'] if params['name'] is not None else historical_place['name']
                historical_place['description'] = params['description'] if params['description'] is not None else historical_place['description']
                historical_place['district'] = params['district'] if params['district'] is not None else historical_place['district']
                return jsonify({'Historical place updated successfully': historical_place})
            
        return jsonify({'Message': 'Historical place not found'})
    
    
    # Create a DELETE method to delete a specific place based on a given identifier
    def delete(self, id):
        # Delete the historical place with the given id
        for historical_place in historical_places:
            if id == historical_place['id']:
                historical_places.remove(historical_place)
                return jsonify({'Message': 'Historical place deleted successfully'})
            
        return jsonify({'Message': 'Historical place not found'})
    
    
    
class HistoricalPlaceDistrict(Resource):
    def get(self, district):
        district_historical_places = [historical_place for historical_place in historical_places if historical_place['district'].lower() == district.lower()]
        if district_historical_places:
            return jsonify({'historical_places': district_historical_places})
        return jsonify({'Message': 'Invalid district name'})
    
    
# Register api resources to the api service
api.add_resource(HistoricalPlaces, '/historical_places')
api.add_resource(HistoricalPlace, '/historical_places/<int:id>')
api.add_resource(HistoricalPlaceDistrict, '/historical_places/<district>')