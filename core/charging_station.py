import logging
from enum import Enum
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChargingStation:
    def __init__(self, longitude, latitude, price, id, owner):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.id = id
        self.owner = owner
        self.status = ChargingStationStatus.FREE

    def get_message(self):
        return {
            "long": self.longitude,
            "lat": self.latitude,
            "owner": self.owner,
            "price": self.price, 
            "id": self.id,
            "status": self.status
        }


class ChargingStationStatus(Enum):
    FREE = "free"
    OCCUPIED = "occupied"
    CLOSED = "closed"