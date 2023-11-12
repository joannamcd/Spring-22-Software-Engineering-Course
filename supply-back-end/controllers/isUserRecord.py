import mysql.connector


def isUserRecord(fleetManager):
    recordExist = "userExist"

    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="Champ1109//",
        database="team23mysqlsupplydatabase")

    # Finds user in db before creation to enforce no duplicate usernames
    mycursor = mydb.cursor(prepared=True)

    sql = "SELECT * FROM fleetMngrUsers WHERE Username = %s"

    val = fleetManager

    mycursor.execute(sql, (val,))

    result = mycursor.fetchone()
    # if record does not exist user can be created
    if result is None:
        recordExist = "userNotExist"

    return recordExist
