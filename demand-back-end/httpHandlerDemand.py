import json
import logging
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import requests

from controllers.isUserRecord import isUserRecord
from controllers.registerUser import registerUser
from projClasses.Users import TaaSUsers

# Class Logger we can use for debugging our Python service. You can add a parameter here for
# specifying a log file if you want to see a stream of log data in one file.


logging.basicConfig(level=logging.DEBUG)


# BaseHTTPRequestHandler is a class from the http.server python module. http.server is a simple
# module used for creating application servers. BaseHTTPRequestHandler will help us respond to requests that arrive
# at our server, matching a specified hostname and port. For additional documentation on this module,
# you can read: https://docs.python.org/3/library/http.server.html


class httpHdlrCmBackEnd(BaseHTTPRequestHandler):
    # HTTP Response code dictionary
    # Add any additional response codes you might want to use
    # You can look up the codes and their proper uses online
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
        'INTERNAL SEVER ERROR': HTTPStatus.INTERNAL_SERVER_ERROR
    }

    # Here's a function to extract GET parameters from a URL
    def extract_GET_parameters(self):
        # GET parameters are just stored in the path of the request, so we can just urlparse this
        path = self.path
        parsedPath = urlparse(path)
        paramsDict = parse_qs(parsedPath.query)
        logging.info('GET parameters received: ' + json.dumps(paramsDict, indent=4, sort_keys=True))
        return paramsDict

    # Here's a function to extract POST parameters from a POST request
    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    ## GET REQUEST HANDLING ##

    def do_GET(self):
        # self.path here will return us the http request path entered by the client.
        path = self.path
        # Extract the GET parameters associated with this HTTP request and store them in a python dictionary
        paramsDict = self.extract_GET_parameters()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND']
        responseBody = {}

        # This is a root URI or block of code that will be executed when client requests the address:
        # http://localhost:8083.
        if path == '/':
            status = self.HTTP_STATUS_RESPONSE_CODES['OK']
            responseBody['data'] = 'Hello world'

        # Here is where you define your GET endpoints
        # Note that for GET, you should use the "in" format to ensure you still get the correct endpoint
        # even when parameters are included

        # If you want to add more endpoints, simply add more elif statements with the endpoints

        # This will add a response header to the header buffer. Here, we are simply sending back
        # an HTTP response header with an HTTP status code to the client.
        self.send_response(status)
        # This will add a header to the header buffer included in our HTTP response. Here we are specifying
        # the data Content-type of our response from the server to the client.
        self.send_header("Content-type", "text/html")
        # The end_headers method will close the header buffer, indicating that we're not sending
        # any more headers back to the client after the line below.
        self.end_headers()
        # Convert the Key-value python dictionary into a string which we'll use to respond to this request
        response = json.dumps(responseBody)
        logging.info('Response: ' + response)
        # Fill the output stream with our encoded response string which will be returned to the client.
        # The wfile.write() method will only accept bytes data.
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)

    ## POST REQUEST HANDLING ##

    def do_POST(self):
        path = self.path
        # Extract the POST body data from the HTTP request, and store it into a Python
        # dictionary we can utilize inside any of our POST endpoints.
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['NOT_FOUND']

        responseBody = {}
        # These path endpoints can be very picky sometimes, and are very much connected to how your DevOps
        # has configured your web server. You will need to communicate with your DevOps to decide on these

        # endpoint for TaasUser
        if path == '/taasUserRegister':
            # This is where you'll implement your actual service logic
            # Process any POST data you are expecting to receive
            response = "userNotCreated"

            taaSUser = TaaSUsers(postBody.get("firstName"),
                                 postBody.get("lastName"),
                                 postBody.get("email"),
                                 postBody.get("username"),
                                 postBody.get("password"),
                                 postBody.get("address"),
                                 postBody.get("city"),
                                 postBody.get("zip"),
                                 postBody.get("state"),
                                 postBody.get("phone"))

            # Collect any data you want to send back into a dictionary and send it back in the responseBody
            isUserExist = isUserRecord(taaSUser.user_name)
            if isUserExist == "userNotExist":
                response = registerUser(taaSUser)
            elif isUserExist == "userExist":
                response = isUserExist

            # three responses to frontend userCreated, userExist, or userNotCreated.
            # userCreated user was created in DB
            # userExist meaning username is already taken in DB
            # userNotCreated pointing to some backend issue preventing trying to write to DB.
            responseBody['data'] = response

            status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        elif path == '/order':
            # This is where you'll implement your actual service logic
            # Process any POST data you are expecting to receive
            # response = "orderNotCreated"

            url = 'https://supply.team23.sweispring22.gq/vehicleRequest'
            route = {'pickup_address': postBody.get('pickup_address'), 'destination_address': postBody.get('destination_address')}
            routeJson = json.dumps(route, indent=4, sort_keys=True, default=str)
            routeInfo = requests.post(url, data=routeJson)

            routeInfoDict = routeInfo.json()

            vehicleID = routeInfoDict['data'].get('vehicleID')
            vehicleCoord = routeInfoDict['data'].get('vehicleCoord')
            pickupCoord = routeInfoDict['data'].get('pickupCoord')
            destCoord = routeInfoDict['data'].get('destCoord')
            timeToPickup = routeInfoDict['data'].get('timeToPickup')
            timeToDest = routeInfoDict['data'].get('timeToDest')
            responseDict = {'vehicleID': vehicleID, 'pickupCoord': pickupCoord, 'destCoord': destCoord, 'vehicleCoord': vehicleCoord, 'timeToPickup': timeToPickup, 'timeToDest': timeToDest}
            response = responseDict

            # Collect any data you want to send back into a dictionary and send it back in the responseBody

            responseBody['data'] = response

            status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # When using the json.dumps() method, you may encounter data types which aren't easily serializable into
        # a string. When working with these types of data you can include an additional parameters in the dumps()
        # method, 'default=str' to let the serializer know to convert to a string when it encounters a data type
        # it doesn't automatically know how to convert.
        response = json.dumps(responseBody, indent=4, sort_keys=True, default=str)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)


# Turn the application server on at the specified port on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Communicate with your DevOps to pick a port for each of your services.
    # Note that ports 0-1023 are reserved and cannot be used.
    serverPort = 8085
    appServer = HTTPServer((hostName, serverPort), httpHdlrCmBackEnd)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
