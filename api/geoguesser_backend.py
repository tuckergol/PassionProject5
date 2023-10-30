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
 (41.3775, 64.5853): "Uzbekistan",
 (15.5527, 48.5164): "Yemen",
 (-9.1900, -75.0152): "Peru",
 (4.2105, 101.9758): "Malaysia",
 (7.2500, -0.0662): "Ghana",
 (-18.6657, 35.5296): "Mozambique",
 (28.3949, 84.1240): "Nepal",
 (-18.8792, 47.5079): "Madagascar"
 (7.5400, -5.5471): "Côte d'Ivoire",
 (6.4238, -66.5897): "Venezuela",
 (5.9641, 12.6533): "Cameroon",
 (17.6078, 8.0817): "Niger",
 (-25.2744, 133.7751): "Australia",
 (40.3399, 127.5101): "North Korea",
 (23.6978, 120.9605): "Taiwan",
 (17.5707, -3.9962): "Mali",
 (12.2383, -1.5616): "Burkina Faso",
 (34.8021, 38.9968): "Syria",
 (7.8731, 80.7718): "Sri Lanka",
 (-13.2543, 34.3015): "Malawi",
 (-13.1339, 27.8493): "Zambia",
 (45.9432, 24.9668): "Romania",
 (-35.6751, -71.543): "Chile",
 (48.0196, 66.9237): "Kazakhstan",
 (15.4542, 18.7322): "Chad",
 (-1.2921, 36.8219): "Kenya",
 (18.3358, -64.8963): "Netherlands",
 (12.5657, 104.9909): "Cambodia",
 (-19.0154, 29.1549): "Zimbabwe",
 (9.9456, -9.6966): "Guinea",
 (-1.9403, 29.8739): "Rwanda",
 (9.3077, 2.3158): "Benin",
 (-3.3731, 29.9189): "Burundi",
 (33.9391, 9.5375): "Tunisia",
 (-16.2902, -63.5887): "Bolivia",
 (18.9712, -72.2852): "Haiti",
 (50.8503, 4.3517): "Belgium",
 (30.5852, 36.2384): "Jordan",
 (18.7357, -70.1627): "Dominican Republic",
 (21.5218, -77.7812): "Cuba",
 (6.8770, 31.3070): "South Sudan",
 (60.1282, 18.6435): "Sweden",
 (15.1990, -86.2419): "Honduras",
 (49.8175, 15.4729): "Czech Republic (Czechia)",
 (40.1431, 47.5769): "Azerbaijan",
 (39.0742, 21.8243): "Greece",
 (-6.314993, 143.955550): "Papua New Guinea",
 (39.3999, -8.2245): "Portugal",
 (47.1625, 19.5033): "Hungary",
 (38.8610, 71.2761): "Tajikistan",
 (23.4241, 53.8478): "United Arab Emirates",
 (53.7098, 27.9534): "Belarus",
 (31.0461, 34.8516): "Israel",
 (8.6195, 0.8248): "Togo",
 (47.5162, 14.5501): "Austria",
(46.8182, 8.2275): "Switzerland",


}



