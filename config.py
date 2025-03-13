from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from scipy import stats

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Statistical Calculator API is running'})


@app.route('/calculate/descriptive')
def calculate_descriptive():
    try:
        data = request.json['numbers']
        result = {
            'mean': np.mean(data),
            'median': np.median(data),
            'mode': stats.mode(data)[0][0],
            'variance': np.var(data),
            'std_dev': np.std(data)
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
