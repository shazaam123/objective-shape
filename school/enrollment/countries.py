from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/api/countries', methods=['GET'])
def get_countries():
    with open('countries.json', 'r') as f:
        country_code = json.load(f)
    return jsonify(country_code), 200


@app.route('/api/country/<country_name>', methods=['GET'])
def get_country_code(country_name):
    with open('countries.json', 'r') as f:
        country_code = json.load(f)
    country_code = country_code.get(country_name, "Unknown")
    return jsonify({country_name: country_code}), 200

if __name__ == "__main__":
    app.run(debug=True)
