from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data')
def get_data():
    with open('currStats.txt', 'r') as f:
        paper = int(f.readline().strip())
        metal = int(f.readline().strip())
        plastic = int(f.readline().strip())

    return jsonify({'papers': paper, 'metals': metal, 'plastics': plastic})

if __name__ == '__main__':
    app.run(debug=True)
