from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

hospitals_bp = Blueprint('hospitals', __name__)
api = Api(hospitals_bp)

# Create a dictionary of hospitals
hospitals = [
    {"id": 0, "name": "Kamuzu Central Hospital", "district": "Lilongwe","location": "Lilongwe city", "beds": 1000, "doctors": 100,"nurses":200},
    {"id": 1, "name": "Queen Elizabeth Central Hospital", "district": "Blantyre", "location": "Blantyre city", "beds": 1000, "doctors": 100, "nurses": 200},
    {"id": 2, "name": "Mzuzu Central Hospital", "district": "Mzuzu", "location": "Mzuzu city", "beds": 1000,"doctors": 100,"nurses": 200}
]


# Create a class and method for getting all hospitals
class Hospitals(Resource):
    def get(self):
        return jsonify({'hospitals': hospitals})
    
    
    # Create a POST method for adding new hospitals to the list
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Hospital id is required')
        parser.add_argument('name', type=str, required=True, help='Hospital name is required')
        parser.add_argument('district', type=str, required=True, help='Hospital district is required')
        parser.add_argument('location', type=str, required=True, help='Hospital location is required')
        parser.add_argument('beds', type=int, required=True, help='Hospital beds are required')
        parser.add_argument('doctors', type=int, required=True, help='Hospital doctors are required')
        parser.add_argument('nurses', type=int, required=True, help='Hospital nurses are required')
        params = parser.parse_args()
        
        for hospital in hospitals:
            if params['id'] == hospital['id']:
                return jsonify({'Message': 'Hospital with id {} already exists'.format(params['id'])})
    
        hospital = {
                    'id': params['id'],
                    'name': params['name'],
                    'district': params['district'],
                    'location': params['location'],
                    'beds': params['beds'],
                    'doctors': params['doctors'],
                    'nurses': params['nurses']
                }
                
        hospitals.append(hospital)
        return jsonify({'Hospital added successfully': hospital, 'status': 201})
        
        


# Create a class and method for getting all hospitals in a particular district
class Hospital(Resource):
    def get(self, id):
        hospital = [hospital for hospital in hospitals if hospital['id'] == id]
        if hospital:
            return jsonify({'hospital': hospital})
        return jsonify({'Message': 'Hospital not found'})
    
    
    # Create a PUT method for updating a hospital based on the id provided
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('district', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('beds', type=int)
        parser.add_argument('doctors', type=int)
        parser.add_argument('nurses', type=int)
        params = parser.parse_args()
        
        hospital = [hospital for hospital in hospitals if hospital['id'] == id]
        if not hospital:
            return jsonify({'Message': 'Hospital not found'})
        else:
            hospital = hospital[id]
            hospital[0]['name'] = params['name'] if params['name'] is not None else hospital['name']
            hospital[0]['district'] = params['district'] if params['district'] is not None else hospital['district']
            hospital[0]['location'] = params['location'] if params['location'] is not None else hospital['location']
            hospital[0]['beds'] = params['beds'] if params['beds'] is not None else hospital['beds']
            hospital[0]['doctors'] = params['doctors'] if params['doctors'] is not None else hospital['doctors']
            hospital[0]['nurses'] = params['nurses'] if params['nurses'] is not None else hospital['nurses']
            return jsonify({'Hospital updated successfully': hospital[0]})



# Create a class and method for getting a single hospital by its id
class HospitalDistrict(Resource):
    def get(self, district):
        district_hospitals = [hospital for hospital in hospitals if hospital['district'].lower() == district.lower()]
        if district_hospitals:
            return jsonify({'hospitals': district_hospitals})
        return jsonify({'Message': 'Invalid district name'})
    

# Register the resources to the api service
api.add_resource(Hospitals, '/hospitals')
api.add_resource(Hospital, '/hospitals/<int:id>')
api.add_resource(HospitalDistrict, '/hospitals/<district>')