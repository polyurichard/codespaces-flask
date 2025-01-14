from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# define an endpoint that returns a random number as a JSON object
@app.route("/random")
def random_number():
    import random
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return response

@app.route('/temperature', methods=['GET'])
def get_temperature():
    # HKO API URL for temperature data
    hko_api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

    # Fetch data from HKO API
    response = requests.get(hko_api_url)
    data = response.json()

    # Extract temperature data
    temperature_data = data.get('temperature', {}).get('data', [])

    # Format the response
    temperature_info = [
        {
            'place': location['place'],
            'temperature': location['value']
        }
        for location in temperature_data
    ]

    return jsonify(temperature_info)