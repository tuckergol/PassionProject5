# api.py
from flask import Flask, request, jsonify
from model import countries, get_country_info

app = Flask(__name__)

@app.route('/api/geoguesser/country-info/<country_name>', methods=['GET'])
def get_country_info_route(country_name):
    country_info = get_country_info(country_name)
    if country_info:
        return jsonify(country_info)
    return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086)
s
