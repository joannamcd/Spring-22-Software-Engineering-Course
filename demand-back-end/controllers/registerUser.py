import mysql.connector


def registerUser(TaaSUsers):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="passwordgoeshere",
        database="team23DemandDatabase")

    # Adds TaasUser to mySQL DB
    mycursor = mydb.cursor()

    sql = "INSERT INTO users " \
          "(First_Name, " \
          "Last_Name," \
          "Email," \
          "Username," \
          "Phone," \
          "Password," \
          "Address," \
          "City," \
          "Zip," \
          "State)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (TaaSUsers.first_name,
           TaaSUsers.last_name,
           TaaSUsers.email,
           TaaSUsers.user_name,
           TaaSUsers.phone,
           TaaSUsers.password,
           TaaSUsers.home_address,
           TaaSUsers.city,
           TaaSUsers.zipcode,
           TaaSUsers.state)

    mycursor.execute(sql, val)

    mydb.commit()

    return "userCreated"
