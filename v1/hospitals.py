from flask import Blueprint, jsonify

hospitals_bp = Blueprint('hospitals', __name__)

# Create a dictionary of hospitals
hospitals = [
    {
        "id": 1,
        "name": "Kamuzu Central Hospital",
        "district": "Lilongwe",
        "location": "Lilongwe city",
        "beds": 1000,
        "doctors": 100,
        "nurses": 200
    },
    {
        "id": 2,
        "name": "Queen Elizabeth Central Hospital",
        "district": "Blantyre",
        "location": "Blantyre city",
        "beds": 1000,
        "doctors": 100,
        "nurses": 200
    },
    {
        "id": 3,
        "name": "Mzuzu Central Hospital",
        "district": "Mzuzu",
        "location": "Mzuzu city",
        "beds": 1000,
        "doctors": 100,
        "nurses": 200
    }
]


# Create a route for getting all hospitals
@hospitals_bp.route('/hospitals', methods=['GET'])
def get_all_hospitals():
    return jsonify({'hospitals': hospitals})


# Create a route for getting all hospitals in a particular district
@hospitals_bp.route('/hospitals/<district>', methods=['GET'])
def get_hospitals(district):
    # filter the hospitals by district
    district_hospitals = [hospital for hospital in hospitals if hospital['district'].lower() == district.lower()]
    return jsonify({'hospitals': district_hospitals})