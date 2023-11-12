# README #

### What is this repository for? ###

* Storing files for Map Services support

### How do I get set up? ###

* Documentation is saved on Google Drive
* Any code involved in testing map services will be committed to the repository

### Working with the repository ###

* Clone the repository to your local machine
* Test changes locally before commiting them to the repo
* Commit changes to the feature branch
* On Bitbucket:
    * Approve the commit
    * Create a pull request to pull from the feature branch to the dev branch
    * Merge the branches
* On the droplet (demand for customer facing map, supply for fleet manager facing map):
    * SSH to the droplet (contact DevOps for an account if necessary)
    * Change directory to /home/team23/repos/map-services
    * run 'git checkout --force dev' to make sure you're pulling from the dev branch
    * run 'git pull' to pull changes from the repo

### Who do I talk to? ###

* Team 23 TM3 Nick Enghardt

### Where can I find information about working with MapBox Maps? ###

* We use MapBox GL JS to create maps
* Install guide: https://docs.mapbox.com/mapbox-gl-js/guides/install/
* Starting with a simple map: https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
* Use the left navigation menu on the MapBox site to walk through guides on:
** Changing map properties
** Working with map markers