import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/weeks')
def get_weeks():
    # Get Airtable credentials from environment variables
    airtable_api_key = os.environ.get('patgGa8Hm0Jv3JjLv')
    airtable_base_id = os.environ.get('appooefq0dgXe7VIw')
    table_name = 'WEEKS'

    if not airtable_api_key or not airtable_base_id:
        return jsonify({"error": "Missing Airtable credentials"}), 500

    # Construct the Airtable API endpoint
    url = f'https://api.airtable.com/v0/{airtable_base_id}/{table_name}'
    headers = {
        'Authorization': f'Bearer {airtable_api_key}'
    }

    # Request all records from the "WEEKS" table
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data", "details": response.json()}), response.status_code

    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    # Render provides the PORT environment variable; default to 8080 if not set.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
