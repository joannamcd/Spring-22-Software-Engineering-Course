class Orders:
    def __init__(self, vehicleID, taas_Username, pickup_address, destination_address, orderID=None):
        self.taas_Username = taas_Username
        self.pickup_address = pickup_address
        self.destination_address = destination_address
        self.vehicleID = vehicleID
        if orderID is None:
            self.orderID = -1
        else:
            self.orderID = orderID
