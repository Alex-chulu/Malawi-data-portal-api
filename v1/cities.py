from flask import Blueprint, jsonify

cities_bp = Blueprint('cities', __name__)


cities = [
        {
        "id": 1,
        "name": "Lilongwe",
         "population": 989748,
         "region": "Central",
         "latitude": "-13.983333",
         "longitude": "33.783333"
         },
        {
        "id": 2,
        "name": "Blantyre",
         "population": 789498,
         "region": "Southern",
         "latitude": "-15.783333",
         "longitude": "35.000000"
         },
        {
        "id": 3,    
        "name": "Mzuzu",
         "population": 189748,
         "region": "Northern",
         "latitude": "-11.466667",
         "longitude": "34.016667"
         }
    ]
    
    # Logic to fetch total population and population by city
@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(cities)

# Return city by id
@cities_bp.route('/cities/<int:id>', methods=['GET'])
def get_city(id):
    city = [city for city in cities if city['id'] == id]
    return jsonify({'city': city})