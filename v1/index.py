from flask import Flask

app = Flask(__name__)

# Initialize the app
@app.route('/')
def index():
    return "Hello, World!"


# Run the app
if __name__ == '__main__':
    app.run(debug=True)