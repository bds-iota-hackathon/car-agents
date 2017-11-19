#!/usr/bin/env python2
# File to test all stuff in the api

from iotawrapper import IotaWrapper
import charging_station as cs
from iota import *
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Test data
url = "http://p103.iotaledger.net:14700"
seed = "QXCAMQVJXGIVZUZMYJZAPFYAFXCCBOBPYDKKUVJDJNNQAEF9NQOIGMAKGGMJLDLMMSTOBAL9PNNUNPIVM"
address = "U9Y9PVIBHONULDYBMY9IXBUAZEGINTZQZOTFIXYECBBPNQXBBOTQOZPCIPQLROKWJJ9UWDTUBTNQVO9RD"

iota = IotaWrapper(url, seed)
logger.info(iota.connect())

print iota.get_balance("U9Y9PVIBHONULDYBMY9IXBUAZEGINTZQZOTFIXYECBBPNQXBBOTQOZPCIPQLROKWJJ9UWDTUBTNQVO9RD")

vendor_seed = "OJJUQWUWCW9LXFBGHIUGXQTUYYOAHJIQMJBBPOHBHCLBYDUMXLNLSUQJLNFMBITGSXGNLPFABLTQDXBM9"
vendor_address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"

customer_seed = "DOUPURWDDAX9NHSVIWQN9NHMHHYFM9LFSEOJANKPHGFSHBFAKCAKDDZV9LYMCHSJFMRZK9IPBOAQNLYNV"
customer_address = "NSNOHLXXXPGJAUUVKZEDUPBEIJDDKA99LPOTSAD9SWKFRIVQKMQRXWMKJRNDIMANTKLZWWEVEWLQATYDB"

# print iota.find_transactions(18, 54, 2)
# print station.advertise_free(iota)

# for stn in cs.FIVE_STATIONS:
#     stn.advertise(iota)
# print iota.find_transactions_local()
# print iota.find_transactions(18, 54, 2)
