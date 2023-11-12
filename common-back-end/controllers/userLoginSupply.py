import bcrypt
import mysql.connector


def userLoginSupplyside(token):
    loginStatus = 'badLogin'

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="Champ1109//",
        database="team23mysqlsupplydatabase",
        auth_plugin='mysql_native_password')

    # Finds users in db for login
    mycursor = mydb.cursor()

    sql = "SELECT Password FROM fleetMngrUsers WHERE Username = %s"

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
