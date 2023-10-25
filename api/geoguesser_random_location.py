from geopy.geocoders import Nominatim
import random

geolocator = Nominatim(user_agent="geo_guesser_app")

# Generate random latitude and longitude coordinates
latitude = random.uniform(-90, 90)
longitude = random.uniform(-180, 180)

# Perform reverse geocoding to get the country
location = geolocator.reverse(f"{latitude}, {longitude}")
address = location.raw

# Extract the country information
country = address.get('address', {}).get('country')

if country:
    print(f"Coordinates: Latitude {latitude}, Longitude {longitude}")
    print(f"Country: {country}")
else:
    print("Country not found for the given coordinates.")
