# README #

This README provides information regarding the WeGO Supply Cloud Vehicle Request API.

### How do I update this repository? ###

* Pull from master branch
* Push to dev branch for testing
* If testing is successful merge dev to master

### What is this repository for? ###

* Quick summary
  * How to send POST requests to the API:
    * Send a POST request to https://supply.team23.sweisprint22.gq/vehicleRequest
    * The request needs to include 2 addresses
      * Pickup Location
      * Destination Location
  * How is the information obtained?
    * The pickup address is sent to the Mapbox Geolocation API
      * GPS coordinates are returned
    * The destination address is sent to the Mapbox Geoloation API
      * GPS coordinates are returned
    * The vehicle and pickup location GPS coordinates are sent to the Mapbox Directions API
      * A route is returned (route1)
    * The pickup and destination GPS coordinates are sent to the Mapbox Directions API
      * A route is returned (route2)
    * The duration of the routes is returned as separate values
  * What is returned by a POST request:
    * Vehicle ID
    * GPS Coordinates for pickup location and destination
    * ETA to the pickup location from the vehicle location
    * ETA to the destination from the pickup location

### How do I get set up? ###

* Clone the vehicleRequestAPI to your local machine
* Use Bitbucket to sync commit to the feature branch
* Test on Dev Branch
* Merge to Master Branch when testing is complete

### Who do I talk to? ###

* Nick Enghardt