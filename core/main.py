# File to test all stuff in the api

from iotawrapper import IotaWrapper
from charging_station import ChargingStation
from iota import *
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test data
url = "https://testnet140.tangle.works:443"
seed = "OJJUQWUWCW9LXFBGHIUGXQTUYYOAHJIQMJBBPOHBHCLBYDUMXLNLSUQJLNFMBITGSXGNLPFABLTQDXBM9"
address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"

iota = IotaWrapper(url, seed)
logger.info(iota.connect())

# logger.info("Trying to add transaction")
# test_address = "ZRJUBCUBQKKE9RRWTIBU9VVGZBZBDQUFSNHJXMMEZVMXIDZKIOYEDA9UERLEUURJLZSMZGEWKSPTBKHMY"
# test_message = TryteString.from_string("{data:[{node:test}]}")
# bundle = iota.send_transfer(
#     transfers=iota.create_transfers(test_address, test_message),
#     inputs=[Address(address, key_index=0, security_level=0)]
# )

# if bundle is not None:
#     logger.info("Bundle: {hash}".format(hash=bundle["bundle"].as_json_compatible()))

# logger.info("Trying to get message by tag")
# logger.info(iota.find_transactions([iota.get_retarded_tag()]))

# 1) Advertise charging station:
def create_station(station):
    station.status = ChargingStation.FREE
    tryte_msg = TryteString.from_string(json.dumps(station.getMessage()))
    bundle = iota.send_transfer(
        transfers=iota.create_transfers(station.owner, tryte_msg, 0),
        inputs=[Address(station.owner, key_index=0, security_level=0)]
    )
    if bundle is not None:
        logger.info("Bundle: {hash}".format(hash=bundle["bundle"].as_json_compatible()))
    

def search_stations(lon, lat):
    
    tx = iota.find_transactions([iota.get_retarded_tag()])
    logger.info(tx)
    return [t for t in tx]

logger.info("Initiating use case test run")


vendor_seed = "OJJUQWUWCW9LXFBGHIUGXQTUYYOAHJIQMJBBPOHBHCLBYDUMXLNLSUQJLNFMBITGSXGNLPFABLTQDXBM9"
vendor_address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"

customer_seed = "DOUPURWDDAX9NHSVIWQN9NHMHHYFM9LFSEOJANKPHGFSHBFAKCAKDDZV9LYMCHSJFMRZK9IPBOAQNLYNV"
customer_address = "NSNOHLXXXPGJAUUVKZEDUPBEIJDDKA99LPOTSAD9SWKFRIVQKMQRXWMKJRNDIMANTKLZWWEVEWLQATYDB"

lat = 54.409532 
lon = 18.574080
price = 0.5 # miota
id = "Teststation"
station = ChargingStation(lon, lat, price, id, vendor_address)

#create_station(station)
search_stations(0.1, 20)