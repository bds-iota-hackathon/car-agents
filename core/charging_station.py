import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class ChargingStation:
    FREE = "free"
    OCCUPIED = "occupied"
    CLOSED = "closed"
    def __init__(self, longitude, latitude, price, id, owner):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.id = id
        self.owner = owner
        self.status = self.FREE

    
    def getMessage(self):
        return {
            "long" : self.longitude,
            "lat" : self.latitude,
            "owner": self.owner,
            "price": self.price, 
            "id": self.id,
            "status": self.status
        }
