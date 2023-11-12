# WeGo Common Back-End
### How it works
Frontend information is sent to the backend, where it can be sent to a database. The backend files are alive in the droplet.
### HTTP Handler
#### httpHdlrCmBackEnd.py
- The purpose of httpHdlrCmBackEnd.py is to function as an HTTP request handler.
- It includes functions for extracting GET and POST parameters, as well as implementing GET and POST request handling.
### Technologies Used
- python 3.8
- JSON
### Controllers Files
#### userLogin.py
- The purpose of userLogin.py is to communicate with the database during login to verify that the user credentials entered are valid and stored within the database.
- Password hashing is used to hash the password entered by a user, which is then compared to the hashed password stored in the database for that user.
- If the login is not valid based upon the database information, the loginStatus will return a bad login.
### projectClasses Files
#### tokenLogin.py
- The purpose of tokenLogin.py is to verify that the username and password entered by a user are valid entries by length.
- The functions verify that the entered values for username and password do not exceed 30 characters.
#### users.py
- The purpose of users.py is to save the information input by a user when creating an account, as well as to create classes and functions for TaaS Users and Fleet Manager users.
- This includes hashing the password input by the user.
- Within the TaaS User class, there are functions to verify that the values entered when creating an account are valid.
- Within the Fleet Manager User class, there are functions to assign a fleet to a Fleet Manager, as well as to add, remove, and print fleets.


