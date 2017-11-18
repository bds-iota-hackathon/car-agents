# File to test all stuff in the api

from core.iotawrapper import IotaWrapper
from iota import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test data
url = "https://testnet140.tangle.works:443"
seed = "OJJUQWUWCW9LXFBGHIUGXQTUYYOAHJIQMJBBPOHBHCLBYDUMXLNLSUQJLNFMBITGSXGNLPFABLTQDXBM9"
address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"

iota = IotaWrapper(url, seed)
logger.info(iota.connect())

logger.info("Trying to add transaction")
test_address = "ZRJUBCUBQKKE9RRWTIBU9VVGZBZBDQUFSNHJXMMEZVMXIDZKIOYEDA9UERLEUURJLZSMZGEWKSPTBKHMY"
test_message = TryteString.from_string("{data:[{node:test}]}")
bundle = iota.send_transfer(
    transfers=iota.create_transfers(test_address, test_message),
    inputs=[Address(address, key_index=0, security_level=0)]
)

if bundle is not None:
    logger.info("Bundle: {hash}".format(hash=bundle["bundle"].as_json_compatible()))

logger.info("Trying to get message by tag")
logger.info(iota.find_transactions([iota.get_retarded_tag()]))