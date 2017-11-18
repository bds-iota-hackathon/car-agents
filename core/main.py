# File to test all stuff in the api

from core.iotawrapper import IotaWrapper
from iota import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test data
url = "https://testnet140.tangle.works:443"
seed = "FNCWNXJWJIVDGPRWNZYKOMKNIIATPPDKEVCZEWSZTEVIWJFCOUV9PJD9AUCEVQLFEAI9UBUAVQKVEBLKN"
address = "DDLAERGKJZCFCICUTHTPZNACYCNCLJMBFK9OKI9BMMWXYVKBYJZRCW9CIIKFJHOCPOQHNAMOOUERZZIHD"

iota = IotaWrapper(url, seed)
print iota.connect()
print TryteString.from_string("CARSHARING")
bundle = iota.send_transfer(
    transfers=[
                ProposedTransaction(
                    address=Address("JEMEHHS9EEASH9UFOLYAKBCTNKGBADCLTKCEOEKPZVILIGTZOGYMFMWKQABVVNKHGHBHTJNRVDDMMUQOX"),
                    value=0,
                    message=TryteString.from_string("Damn it works in Python!"),
                    tag=TryteString.from_string("CARSHARING")
                )
    ],
    inputs=[Address(address, key_index=0, security_level=0)]
)
if bundle is not None:
    print "Bundle: {hash}".format(hash=bundle["bundle"].as_json_compatible())
