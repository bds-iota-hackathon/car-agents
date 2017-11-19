from iota import *
from requests.exceptions import ConnectionError
import json

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IotaWrapper:
    def __init__(self, url, seed):
        self.__url = url
        self.__seed = seed
        self.__node_info = None
        self.__api = None
        self.__tag = "PLUGINBABY"

    def connect(self):
        try:
            self.__api = Iota(self.__url, self.__seed)
            self.__node_info = self.__api.get_node_info()
            logger.info("Node information: {info}".format(info=self.__node_info))
        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))
        else:
            logger.info("Connected.")
            return self.__node_info

    def get_retarded_tag(self):
        # Don't ask, I've wasted 2 hours of making this work
        # IOTA API is great. Seriously.
        tryte_tag = self.__tag
        while len(tryte_tag) < 27:
            tryte_tag += "9"
        return Tag(tryte_tag)

    def create_transfers(self, address, message, value=0):
        return [
            ProposedTransaction(
                # All hail the glory of IOTA and their dummy transactions for tag retrieval.
                address=Address("SQAZ9SXUWMPPVHKIWMZWZXSFLPURWIFTUEQCMKGJAKODCMOGCLEAQQQH9BKNZUIFKLOPKRVHDJMBTBFYW"),
                value = 0
            ),
            ProposedTransaction(
                address=Address(address),
                value=value,
                message=TryteString.from_string(message),
                tag=self.get_retarded_tag()
            )
        ]

    def create_inputs(self, address):
        return [Address(address, key_index=0, security_level=2)]

    def send_transfer(self, transfers, inputs=[], depth=3, min_weight_magnitude=16):
        try:
            if transfers is None:
                logger.error("You need to specify transfers dummy!")
                return
            response = self.__api.send_transfer(
                depth=depth,
                min_weight_magnitude=min_weight_magnitude,
                inputs=inputs,
                transfers=transfers
            )
        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))
        else:
            return response

    # For now looking only using tag, for hackathon needs
    def find_transactions(self, lon, lat, radius):
        try:
            response = self.__api.find_transactions(tags=[TryteString(self.get_retarded_tag())])
            if len(response["hashes"]) == 0:
                return []
            trytes = self.__api.get_trytes(response["hashes"])
            txs = []
            for trytestring in trytes["trytes"]:
                transaction = Transaction.from_tryte_string(trytestring)

                print transaction.timestamp
                print get_current_timestamp()

                if transaction.timestamp > get_current_timestamp() - 1800:
                    txs.append(transaction)

        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))
        else:
            msg_dicts = [json.loads(msg.signature_message_fragment.as_string()) for msg in txs]
            return [msg for msg in msg_dicts if self._within(msg, lon, lat, radius)]

    def _within(self, txd, lon, lat, radius):
        if "long" not in txd or "lat" not in txd:
            return False
        x = txd['long'] - lon
        y = txd['lat'] - lat
        return x * x + y * y < radius ** 2
