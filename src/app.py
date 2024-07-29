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

@app.route('/train_model', methods=['POST'])
def train_model():
    data = request.json['data']
    labels = request.json['labels']
    model = train_deep_learning_model(data, labels)
    return jsonify({'status': 'Model trained successfully'})

if __name__ == '__main__':
    app.run(debug=True)
