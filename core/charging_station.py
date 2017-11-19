import logging
from enum import Enum
import json

from iota import Address, TryteString

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

vendor_address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"


class ChargingStationStatus(Enum):
    FREE = "free"
    OCCUPIED = "occupied"
    CLOSED = "closed"


class ChargingStation:
    def __init__(self, longitude, latitude, price, id, owner,
                 status=ChargingStationStatus.FREE.value):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.id = id
        self.owner = owner
        self.status = status

    def get_message(self):
        return {
            "long": self.longitude,
            "lat": self.latitude,
            "owner": self.owner,
            "price": self.price, 
            "id": self.id,
            "status": self.status
        }

    # Advertise charging station (FREE or OCCUPIED OR CLOSED)
    # Return:   bundle hash
    # Params:
    #   iota:IotaWrapper, the instance to use for sending
    def advertise(self, iota):
        msg = json.dumps(self.get_message())

        bundle = iota.send_transfer(
            transfers=iota.create_transfers(self.owner, msg, 0),
            inputs=[Address(self.owner, key_index=0, security_level=0)]
        )
        return bundle["bundle"].as_json_compatible()

    def __str__(self):
        return ("Station %s (%s) at (%f, %f) " %
                (self.id, self.status, self.latitude, self.longitude))


# This is a monopoly
five_stations_data = [
    [18.5772788, 54.4060541, 3, "ExpensiveStation", vendor_address,
        ChargingStationStatus.FREE.value],
    [18.5772656, 54.404569, 1, "BestStation", vendor_address,
        ChargingStationStatus.OCCUPIED.value],
    [18.578795, 54.406126, 1.3, "FriendlyGarage", vendor_address,
        ChargingStationStatus.FREE.value],
    [18.578126, 54.404454, 1.3, "CoolCharger", vendor_address,
        ChargingStationStatus.FREE.value],
    [18.577074, 54.405355, 1.3, "Favourite", vendor_address,
        ChargingStationStatus.CLOSED.value],
]

FIVE_STATIONS = [ChargingStation(*stnd) for stnd in five_stations_data]
