# src/app.py

from flask import Flask, render_template, request, jsonify
from dimensional_awareness import advanced_quantum_circuit, prepare_ml_data, train_ml_model
from deep_learning_model import train_deep_learning_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_circuit', methods=['POST'])
def run_circuit():
    results = advanced_quantum_circuit()
    return jsonify(results)

@app.route('/prepare_ml_data', methods=['POST'])
def prepare_ml_data_route():
    counts = request.json['counts']
    data, labels = prepare_ml_data(counts)
    return jsonify({'data': data.tolist(), 'labels': labels.tolist()})

@app.route('/train_ml_model', methods=['POST'])
def train_ml_model_route():
    data = request.json['data']
    labels = request.json['labels']
    model = train_ml_model(data, labels)
    return jsonify({'status': 'Logistic Regression Model trained successfully'})

@app.route('/train_deep_learning_model', methods=['POST'])
def train_deep_learning_model_route():
    data = request.json['data']
    labels = request.json['labels']
    model = train_deep_learning_model(data, labels)
    return jsonify({'status': 'Deep Learning Model trained successfully'})

if __name__ == '__main__':
    app.run(debug=True)
