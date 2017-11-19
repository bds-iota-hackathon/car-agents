import logging
from enum import Enum
import json

from iota import Address, TryteString

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

    # Advertise charging station
    # Return:   bundle hash
    # Params:
    #   iota:IotaWrapper, the instance to use for sending
    def advertise_free(self, iota):
        self.status = ChargingStationStatus.FREE.value
        msg = json.dumps(self.get_message())

        bundle = iota.send_transfer(
            transfers=iota.create_transfers(self.owner, msg, 0),
            inputs=[Address(self.owner, key_index=0, security_level=0)]
        )
        return bundle["bundle"].as_json_compatible()


class ChargingStationStatus(Enum):
    FREE = "free"
    OCCUPIED = "occupied"
    CLOSED = "closed"
