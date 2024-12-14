import time
import requests
import random

def read_traffic_data():
    traffic_volume = random.randint(0, 100)
    speed = random.randint(0, 100)
    congestion_level = random.randint(0, 100)
    return traffic_volume, speed, congestion_level

while True:
    traffic_volume, speed, congestion_level = read_traffic_data()
    data = {
        'traffic_volume': traffic_volume,
        'speed': speed,
        'congestion_level': congestion_level
    }
    response = requests.post('http://127.0.0.1:5000/add_traffic_data', json=data)
    print(response.json())
    time.sleep(60)  # Delay for a minute before next reading
