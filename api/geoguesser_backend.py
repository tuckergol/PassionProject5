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


# Define a dictionary mapping coordinates to countries
    country_coordinates = {
    
(28.6139, 77.2090): "India",
 (35.8617, 104.1954): "China",
 (37.7749, -122.4194): "United States",
 (-6.2088, 106.8456): "Indonesia",
 (30.3753, 69.3451): "Pakistan",
 (9.0820, 8.6753): "Nigeria",
 (-15.7801, -47.9292): "Brazil",
 (23.6850, 90.3563): "Bangladesh",
 (55.7558, 37.6176): "Russia",
 (19.4326, -99.1332): "Mexico",
 (9.1450, 40.489673): "Ethiopia",
 (35.682839, 139.759455): "Japan",
 (12.8797, 121.7740): "Philippines",
 (26.8206, 30.8025): "Egypt",
 (-4.0383, 21.7587): "DR Congo",
 (14.0583, 108.2772): "Vietnam",
 (32.4279, 53.6880): "Iran",
 (38.9637, 35.2433): "Turkey",
 (51.1657, 10.4515): "Germany",
 (15.8700, 100.9925): "Thailand",
 (51.5074, -0.1278): "United Kingdom",
 (-6.369028, 34.888822): "Tanzania",
 (48.8566, 2.3522): "France",
 (-30.5595, 22.9375): "South Africa",
 (41.8719, 12.5675): "Italy",
 (-1.286389, 36.817223): "Kenya",
 (21.9162, 95.9560): "Myanmar",
 (4.5709, -74.2973): "Colombia",
 (37.5665, 126.9780): "South Korea",
 (1.3733, 32.2903): "Uganda",
 (12.6392, 29.3328): "Sudan",
 (40.4168, -3.7038): "Spain",
 (-38.4161, -63.6167): "Argentina",
 (28.0339, 1.6596): "Algeria",
 (33.3152, 44.3661): "Iraq",
 (33.9391, 67.7100): "Afghanistan",
 (51.9194, 19.1451): "Poland",
 (56.1304, -106.3468): "Canada",
 (31.7917, -7.0926): "Morocco",
 (23.8859, 45.0792): "Saudi Arabia",
 (48.3794, 31.1656): "Ukraine",
 (-11.2027, 17.8739): "Angola",
 

}



