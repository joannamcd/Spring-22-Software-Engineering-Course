import mysql.connector


def registerUser(fleetManager):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="Champ1109//",
        database="team23mysqlsupplydatabase")

    # Adds fleetManagerUser to mySQL DB
    mycursor = mydb.cursor()

    sql = "INSERT INTO fleetMngrUsers " \
          "(First_Name, " \
          "Last_Name," \
          "Email," \
          "Username," \
          "Phone," \
          "Password," \
          "Assigned_Fleet)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (fleetManager.first_name,
           fleetManager.last_name,
           fleetManager.email,
           fleetManager.user_name,
           fleetManager.phone,
           fleetManager.password,
           fleetManager.assigned_fleets)

    mycursor.execute(sql, val)

    mydb.commit()

    return "userCreated"
