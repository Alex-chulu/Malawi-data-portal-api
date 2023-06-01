from flask import Blueprint, jsonify

districts_bp = Blueprint('districts', __name__)


# Create a dictionary of districts and thier associated data
districts = [
        {
            "id": 1,
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
                    "id": 1,
                    "name": "Lilongwe Girls Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "id": 2,
                    "name": "Kamuzu Academy",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "id": 1,
                    "name": "Kabudula",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "id": 2,
                    "name": "Malingunde",
                    "population": 20000,
                    "males": 6000,
                    "females": 10000,
                    "children": 4000,
                }
            ]
        },
        {
            "id": 2,
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
                    "id": 1,
                    "name": "Blantyre Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "id": 2,
                    "name": "Chichiri Secondary School",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "id": 1,
                    "name": "Chirimba",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "id": 2,
                    "name": "Namiwawa",
                    "males": 6000,
                    "females": 6000,
                    "children": 4000,
                }
            ]
        }
    ]  # Replace with actual data


# Define the routes the districts blueprint will be handling
# This route will be used to get all districts
@districts_bp.route('/districts', methods=['GET'])
def get_districts():
    return jsonify(districts)


# This route will be used to get a particular district
@districts_bp.route('/districts/<int:id>', methods=['GET'])
def get_district(id):
    # filter the districts by id
    district = [district for district in districts if district['id'] == id]
    return jsonify({'district': district})