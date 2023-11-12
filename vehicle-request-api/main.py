import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import urllib.parse
from urllib.request import urlopen
import config
import requests
from mapboxInteractions import getGPS, getDirections, getDuration

logging.basicConfig(level=logging.DEBUG)

class VehicleRequestService(BaseHTTPRequestHandler):
    # HTTP Response code dictionary
    # Add any additional response codes you might want to use
    # You can look up the codes and their proper uses online
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
    }

    # Here's a function to extract POST parameters from a POST request
    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    def do_POST(self):
        path = self.path
        # Extract the POST body data from the HTTP request, and store it into a Python
        # dictionary we can utilize inside any of our POST endpoints.
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND']

        responseBody = {}
        # These path endpoints can be very picky sometimes, and are very much connected to how your DevOps
        # has configured your web server. You will need to communicate with your DevOps to decide on these
        if path == '/vehicleRequest':
            # This is where you'll implement your actual service logic
            # Process any POST data you are expecting to receive

            vehicleID = "Vehicle 12"
            pickupAddress = postBody.get("pickup_address")
            destAddress = postBody.get("destination_address")
            vehicleCoord = [-97.74197567318983, 30.26767853910939]
            pickupCoord = getGPS(pickupAddress)
            destCoord = getGPS(destAddress)
            route1 = getDirections(vehicleCoord, pickupCoord)
            route2 = getDirections(pickupCoord, destCoord)
            timeToPickup = getDuration(route1)
            timeToDest = getDuration(route2)

            responseDict = {"vehicleID": vehicleID, "vehicleCoord": vehicleCoord, "pickupCoord": pickupCoord,
                            "destCoord": destCoord, "timeToPickup": timeToPickup, "timeToDest": timeToDest, "pickupAddress": pickupAddress, "destAddress": destAddress}

            response = responseDict

            url = 'https://supply.team23.sweispring22.gq/vehicleDBUpdate'
            route = responseDict
            routeJson = json.dumps(route, indent=4, sort_keys=True, default=str)
            routeInfo = requests.post(url, data=routeJson)

            routeInfoDict = routeInfo.json()

            # print(routeInfoDict['data'])

            # set status to OK before sending the request so status does not default to 'NOT_FOUND'
            status = self.HTTP_STATUS_RESPONSE_CODES['OK']
            # Collect any data you want to send back into a dictionary and send it back in the responseBody
            responseBody['data'] = response

        # This will add a response header to the header buffer. Here, we are simply sending back
        # an HTTP response header with an HTTP status code to the client.
        self.send_response(status)
        # This will add a header to the header buffer included in our HTTP response. Here we are specifying
        # the data Content-type of our response from the server to the client.
        self.send_header("Content-type", "application/json")
        # The end_headers method will close the header buffer, indicating that we're not sending
        # any more headers back to the client after the line below.
        self.end_headers()
        # Convert the Key-value python dictionary into a string which we'll use to respond to this request
        # When using the json.dumps() method, you may encounter data types which aren't easily serializable into
        # a string. When working with these types of data you can include an additional parameters in the dumps()
        # method, 'default=str' to let the serializer know to convert to a string when it encounters a data type
        # it doesn't automatically know how to convert.
        response = json.dumps(responseBody, indent=4, sort_keys=True, default=str)
        logging.info('Response: ' + response)
        # The wfile.write() method will only accept bytes data, so convert your response to bytes
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)  # then this will send it back to the user


# Turn the application server on at the specified port on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Communicate with your DevOps to pick a port for each of your services.
    # Note that ports 0-1023 are reserved and cannot be used.
    serverPort = 8082
    appServer = HTTPServer((hostName, serverPort), VehicleRequestService)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
