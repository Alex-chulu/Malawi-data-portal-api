from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

# Initialize the app
@app.route('/')
def index():
    return "Hello, World!"


# Create a method that returns the population
@app.route('/malawi')
def get():
    return {'Malawi Population': 19129952}

# Run the app
if __name__ == '__main__':
    app.run(debug=True)