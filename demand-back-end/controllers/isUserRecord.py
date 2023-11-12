import mysql.connector


def isUserRecord(taaSUsername):
    recordExist = "userExist"

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="passwordgoeshere",
        database="team23DemandDatabase")

    # Finds user in db before creation to enforce no duplicate usernames
    mycursor = mydb.cursor(prepared=True)

    sql = "SELECT * FROM users WHERE Username = %s"

    val = taaSUsername

    mycursor.execute(sql, (val,))

    result = mycursor.fetchone()
    # if record does not exist user can be created
    if result is None:
        recordExist = "userNotExist"

    return recordExist
