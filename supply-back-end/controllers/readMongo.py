from pymongo import MongoClient


def readMongoCollection():
    client = MongoClient("mongodb://admin:admin123@localhost:27017")
    db = client.team23supply
    try:
        db.command("serverStatus")
    except Exception as e:
        print(e)
    else:
        print("You are connected!")

    col = db["route"]
    route = col.find_one({"vehicleID": 12})
    client.close()
    return route
