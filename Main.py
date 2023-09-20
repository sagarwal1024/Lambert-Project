import requests
import json

#API key
key = "AIzaSyBwcpy0wOXPN0T0CihmbQKyijY5_cgoCYQ"

#inputs for place
home = input("Enter start address\n")
dest = input("Enter end address\n")
emission = input("What is the emission of the car?\n")

#base url
url = "https://routes.googleapis.com/directions/v2:computeRoutes?key=" + key

data = {
    'origin': {
        'address': home
    },
    'destination': {
        'address': dest
    },
    'travelMode': 'DRIVE',
    'languageCode': 'en-US',
    'routingPreference': 'TRAFFIC_AWARE_OPTIMAL',
    'requestedReferenceRoutes': 'FUEL_EFFICIENT',
    "routeModifiers": {
        "vehicleInfo": {
            "emissionType": emission
        }
    },

}

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': 'AIzaSyBwcpy0wOXPN0T0CihmbQKyijY5_cgoCYQ',
    'X-Goog-FieldMask': 'routes.distanceMeters,routes.duration,routes.polyline.encodedPolyline,routes.routeLabels,routes.routeToken'
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Extract the duration in seconds from the response
    duration_in_seconds = response_data['routes'][0]['duration']

    print(duration_in_seconds)
else:
    print("Error:", response.status_code)