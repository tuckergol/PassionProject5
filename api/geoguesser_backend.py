from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim  # Geocoding library

app = Flask(__name__)

geolocator = Nominatim(user_agent="geo_guesser_app")  # Initialize the geocoder

@app.route('/api/get_country', methods=['POST'])
def get_country():
    try:
        # Get latitude and longitude from the POST request
        data = request.get_json()
        lat = float(data.get('latitude'))
        lon = float(data.get('longitude'))

        # Perform reverse geocoding to get the country
        location = geolocator.reverse(f"{lat}, {lon}")
        address = location.raw

        # Extract the country information
        country = address.get('address', {}).get('country')

        if country:
            return jsonify({"country": country})
        else:
            return jsonify({"error": "Country not found for the given coordinates."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
