from pymongo import MongoClient


def updateMongoCollection(routeUpdate):
    client = MongoClient("mongodb://admin:admin123@localhost:27017")
    db = client.team23supply
    try:
        db.command("serverStatus")
    except Exception as e:
        print(e)
    else:
        print("You are connected!")

    col = db["route"]

    filterQuery = {"vehicleID": 12}
    newValues = {"$set": {'pickupAddress': routeUpdate.get('pickupAddress')}}
    col.update_one(filterQuery, newValues)

    newValues = {"$set": {"pickupAddress": routeUpdate.get('pickupAddress')}}
    col.update_one(filterQuery, newValues)

    newValues = {"$set": {"destAddress": routeUpdate.get('destAddress')}}
    col.update_one(filterQuery, newValues)

    newValues = {"$set": {"pickupCoord": routeUpdate.get('pickupCoord')}}
    col.update_one(filterQuery, newValues)

    newValues = {"$set": {"destCoord": routeUpdate.get('destCoord')}}
    col.update_one(filterQuery, newValues)

    newValues = {"$set": {"timeToPickup": routeUpdate.get('timeToPickup')}}
    col.update_one(filterQuery, newValues)

    client.close()
