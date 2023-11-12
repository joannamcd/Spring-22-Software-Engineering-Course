import urllib.parse
from urllib.request import urlopen
import json
import config

# Receives an address as a text string
# Returns an array of GPS coordinates
# formatRequestURL function concatenates the submitted values, formats them using URL + UTF8 encoding,
# concatenates the URL and returns it.
# returns LongLat coordinate pair
def getGPS(address):
    # Define parts of the queryAddress that will be encoded into URL-UTF-8 format
    seperator = ", "
    # Define the base URL expected by the API:
    baseURL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
    # sending the access token from a file rather than plain text:
    accessToken = config.key
    # queryAddress = streetAddress + seperator + city + seperator + state + " " + zip
    # encode the address into URL-UTF-8 format
    apiQuery = urllib.parse.quote(address) + ".json?"
    # concatenate the request URL that will be sent to MapBox
    requestURL = baseURL + apiQuery + accessToken
    # print("geolocation request url: ", requestURL)
    # open the request URL
    urlResponse = urlopen(requestURL)
    # store the response from MapBox
    apiResponse = json.loads(urlResponse.read())
    # return the GPS coordinate pair
    return apiResponse['features'][0]['geometry']['coordinates']

# Receives 2 arrays of GPS coordinates
# Returns a route as a json object
# example directions api url:
# https://api.mapbox.com/directions/v5/mapbox/driving/-97.75833%2C30.23038%3B-97.745471%2C30.304875?alternatives=false&annotations=duration&geometries=geojson&language=en&overview=full&steps=true&{access_token}
def getDirections(start, end):
    # Define the base URL expected by the API:
    baseURL = "https://api.mapbox.com/directions/v5/mapbox/driving/"
    # parse the GPS coordinates from the coordinate arrays passed to the function and format them to the API's expectations
    gpsCoordinates = urllib.parse.quote(str(start[0]) + "," + str(start[1]) + ";" + str(end[0]) + "," + str(end[1]))
    # Define the parameters and format them as expected by the API
    params = "?alternatives=false&annotations=duration&geometries=geojson&language=en&overview=full&steps=true&"
    # Add the API access token for authentication and billing
    accessToken = config.key
    # Concatenate the request URL
    requestURL = baseURL + gpsCoordinates + params + accessToken
    # Open the request URL:
    urlResponse = urlopen(requestURL)
    # Store the API response (a route) a json object
    apiResponse = json.loads(urlResponse.read())
    # Return the response (a route)
    return apiResponse

# receives a route
# returns time in HH:MM:SS
# Pulls the duration as a float, uses divmod to get hours, minutes, seconds
def getDuration(route):
    duration = (route['routes'][0]['legs'][0]['duration'])
    mon, sec = divmod(duration, 60)
    hr, mon = divmod(mon, 60)

    return "%d:%02d:%02d" % (hr, mon, sec)