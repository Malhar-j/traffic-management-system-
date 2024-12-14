from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)
CORS(app)

# Mock data to simulate smart contract interactions
mock_traffic_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_traffic_data', methods=['POST'])
def add_traffic_data():
    traffic_volume = request.json['traffic_volume']
    speed = request.json['speed']
    congestion_level = request.json['congestion_level']
    traffic_record = {
        'timestamp': time.time(),
        'trafficVolume': traffic_volume,
        'speed': speed,
        'congestionLevel': congestion_level
    }
    mock_traffic_data.append(traffic_record)
    return jsonify({'message': 'Data added', 'data': traffic_record})

@app.route('/get_traffic_data', methods=['GET'])
def get_traffic_data():
    return jsonify(mock_traffic_data)

@app.route('/adjust_signal_timings', methods=['GET'])
def adjust_signal_timings():
    adjustment = ""
    if not mock_traffic_data:
        adjustment = 'No data available'
    else:
        latest_data = mock_traffic_data[-1]
        if latest_data['congestionLevel'] > 70:
            adjustment = 'Increase green light duration'
        elif latest_data['congestionLevel'] < 30:
            adjustment = 'Decrease green light duration'
        else:
            adjustment = 'Maintain current settings'
    return jsonify({'adjustment': adjustment})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
