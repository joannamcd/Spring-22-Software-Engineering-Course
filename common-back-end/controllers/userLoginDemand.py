import bcrypt
import mysql.connector


def userLoginDemandside(token):
    loginStatus = 'badLogin'

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="passwordgoeshere",
        database="team23DemandDatabase")

    # Finds users in db for login
    mycursor = mydb.cursor(prepared=True)

    sql = "SELECT Password FROM users WHERE Username = %s"

    val = token.user_name

    mycursor.execute(sql, (val,))

    result = mycursor.fetchone()

    # compares given password against hash
    if result is not None:
        hashPass = result[0]
        hashPass = hashPass.encode('utf-8')
        encodedPass = token.password.encode('utf-8')
        if bcrypt.checkpw(encodedPass, hashPass):
            loginStatus = 'goodLogin'

    # return recordExist
    return loginStatus
