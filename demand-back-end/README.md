# README
# What is this repository for?
- Here is where python code that handles http requests lives
## Working with the repository
-   Clone the repository to your local machine
-   Test changes locally before committing them to the repo
-   Commit changes to the feature branch
-   On Bitbucket:
    -   Approve the commit
    -   Create a pull request to pull from the feature branch to the dev branch
    -   Merge the branches
-   On the droplet (demand for customer facing map, supply for fleet manager facing map):
    -   SSH to the droplet (contact DevOps for an account if necessary)
    -   Change directory to /home/team23/repos/map-services
    -   run 'git checkout --force dev' to make sure you're pulling from the dev branch
    -   run 'git pull' to pull changes from the repo
## Who do I talk to?
-  Team 23 TM3 James Ross
## Endpoints List
- /taasUserRegister
- /order