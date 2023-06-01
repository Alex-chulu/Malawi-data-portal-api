from flask import Blueprint, jsonify

districts_bp = Blueprint('districts', __name__)

# Define the routes the districts blueprint will be handling
@districts_bp.route('/districts', methods=['GET'])
def get_districts():
    # Logic to fetch total population and population of districts
    districts = [
        {
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
                    "name": "Lilongwe Girls Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "name": "Kamuzu Academy",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "name": "Kabudula",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "name": "Malingunde",
                    "population": 20000,
                    "males": 6000,
                    "females": 10000,
                    "children": 4000,
                }
            ]
        },
        {
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
                    "name": "Blantyre Secondary School",
                    "teachers": 100,
                    "students": 2000
                },
                {
                    "name": "Chichiri Secondary School",
                    "teachers": 50,
                    "students": 500
                }
            ],
            "villages": [
                {
                    "name": "Chirimba",
                    "population": 10000,
                    "males": 5000,
                    "females": 5000,
                    "children": 2000,
                },
                {
                    "name": "Namiwawa",
                    "males": 6000,
                    "females": 6000,
                    "children": 4000,
                }
            ]
        }
    ]  # Replace with actual data

    return jsonify(districts)