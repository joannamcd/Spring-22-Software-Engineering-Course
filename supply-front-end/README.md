# WeGo Supply Front-End #

### What is this repository for? ###

* VCS for the Supply Cloud's front end
    * Fleet Manager Login
    * Fleet Manager Dashboard

### How do I get set up? ###

* Clone the repo from Bitbucket to your local machine
* Run tests locally before committing changes to the repo
* Commit changes to the feature branch
* On Bitbucket:
    * Approve the commit
    * Set up pull request from feature branch to dev branch
    * Merge the pull request
* On the Supply Droplet (supply.team23.sweispring22.gq):
    * SSH to the droplet
    * Change directory to /home/team23/repos/supply-front-end
    * run 'git checkout --force dev' to make sure you're pulling from the dev branch
    * run 'git pull' to pull changes from the dev branch to the server

### Who do I talk to? 
* Jacob Brandis - Team 23 Frontend developer
* Other community or team contacts:
    * John Salinas - Team 23 DevOps
    * James Ross - Team 23 Backend developer
    * Nick Enghardt - Team 23 Map Services developer
    * Joanna McDonald - Team 23 UI/Frontend developer

### Files in our Supply-side Frontend:
#### fleetManagerCreateAccount.html
- The purpose of fleetManagerCreateAccount.html is for Fleet Managers to be able to fill out a form and create an account. The file then sends their information to our backend which will add their credentials to the supply side SQL database.
#### fleetManagerDashboard.html
- The purpose of fleetManagerDashboard.html is for Fleet Managers to view on a dynamic map the multiple fleets assigned to them and manage them.