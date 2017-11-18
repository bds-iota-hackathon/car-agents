# File to test all stuff in
from core.iotawrapper import IotaWrapper
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test data
url = "https://testnet140.tangle.works:443"
seed = "BSWBJXJUMMFTIDUKXXDKLEXCLKN9TCPORCWVJKEBATJXQTUFTJOBISFDMVPNILHXILOTZEQYKRM9USBNI"

iota = IotaWrapper(url, seed)
if iota.connect():
    # Do something here
    pass
else:
    logger.info("Shutting down app")
