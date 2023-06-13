"""_summary_
This is the main file running the entire application
The main file contains the following:
    - Import the Flask class and other modules
    - Flask app
    - Blueprints
    - Run the app
"""
from flask import Flask
from v1.population import population_bp
from v1.districts import districts_bp
from v1.cities import cities_bp
from v1.historical_places import historical_places_bp
from v1.hospitals import hospitals_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(population_bp, url_prefix='/v1')
app.register_blueprint(districts_bp, url_prefix='/v1')
app.register_blueprint(cities_bp, url_prefix='/v1')
app.register_blueprint(historical_places_bp, url_prefix='/v1')
app.register_blueprint(hospitals_bp, url_prefix='/v1')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)