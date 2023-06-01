from flask import Blueprint, jsonify

population_bp = Blueprint('population', __name__)


@population_bp.route('/population', methods=['GET'])
def get_population():
    # Logic to fetch total population and population by region
    total_population = 19129952
    region_population = [
        {"region": "Northern", "population": 3593479},
        {"region": "Central", "population": 12173448},
        {"region": "Southern", "population": 3433045}
    ]
    
    response = {
        "total_population": total_population,
        "region_population": region_population
    }
    return jsonify(response)