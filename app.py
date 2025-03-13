from flask import Flask, request, jsonify
from services.descriptive import calculate_descriptive
from services.regression import calculate_regression
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Statistical Calculator API is running'})

@app.route('/calculate/descriptive', methods=['POST'])
def descriptive_statistics():
    data = request.json.get('numbers', [])
    return jsonify(calculate_descriptive(data))

@app.route('/calculate/regression', methods=['POST'])
def regression_analysis():
    X = request.json.get('X', [])
    y = request.json.get('y', [])
    return jsonify(calculate_regression(X, y))

if __name__ == '__main__':
    app.run(debug=True)