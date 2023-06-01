from flask import Blueprint, jsonify 

historical_places_bp = Blueprint('historical_places', __name__)

# Create route to access historical places
@historical_places_bp.route('/historical_places', methods=['GET'])
def get_historical_places():
    # Logic to fetch historical places in Malawi
    historical_places = [
        {
            "id": 1,
            "name": "Chongoni Rock Art Area",
            "description": "Chongoni Rock Art Area is a UNESCO World Heritage Site located in Central Malawi, Africa. It was first designated in 2006. The site contains the most concentrated cluster of rock art found in Central Africa. It is situated on a plateau overlooking the Malawi Rift Valley.",
            "location": "Dedza"
        },
        {
            "id": 2,
            "name": "Lake Malawi National Park",
            "description": "Lake Malawi National Park is a national park located in Malawi at the southern end of Lake Malawi. It is the only national park in Malawi that was created to protect fish and aquatic habitats. Despite this, Lake Malawi National Park includes a fair amount of land, including several small islands in Lake Malawi. The park is home to many hundreds of fish species, nearly all endemic.",
            "location": "Mangochi"
        },
        {
            "id": 3,
            "name": "Mua Mission",
            "description": "Mua Mission is a Catholic mission in Malawi, located in the village of Mua. It was founded in 1902 by the White Fathers. The mission is known for its woodcarvings and the Chamare Museum, which is located on the mission grounds. The museum is known for its collection of Gule Wamkulu masks, which are used in the Gule Wamkulu dance of the Chewa people.",
            "location": "Dedza"
        },
        {
            "id": 4,
            "name": "Livingstonia Mission",
            "description": "Livingstonia Mission is a mission station of the Church of Central Africa Presbyterian in northern Malawi, south of the town of Chitimba and close to the lake shore. It was founded by missionaries from the Free Church of Scotland in 1894 and named after the Scottish missionary and explorer David Livingstone. The mission was built on a high plateau, 900 metres above Lake Malawi, overlooking the Rift Valley and Nyika Plateau.",
            "location": "Rumphi"
        }
    ]
    return jsonify(historical_places)