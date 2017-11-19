from iota import *
from requests.exceptions import ConnectionError
from charging_station import FIVE_STATIONS
import json

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IotaWrapper:
    IOTA_TAG = "PLUGINBABY"

    def __init__(self, url, seed):
        self.__url = url
        self.__seed = seed
        self.__node_info = None
        self.__api = None

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

    @staticmethod
    def get_tag():
        tryte_tag = IotaWrapper.IOTA_TAG
        tryte_tag += '9' * (27 - len(tryte_tag))
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
                tag=self.get_tag()
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
    # IOTA's find_transaction can't filter by time.
    def get_app_transactions(self):
        response = self.__api.find_transactions(tags=[TryteString(IotaWrapper.get_tag())])

        if len(response["hashes"]) < 1:
            return []
        return self.__api.get_trytes(response["hashes"])

    def find_transactions(self, lon, lat, radius):
        try:
            trytes = self.get_app_transactions()
            txs = []
            for trytestring in trytes["trytes"]:
                transaction = Transaction.from_tryte_string(trytestring)

                if transaction.timestamp > get_current_timestamp() - 1800:
                    txs.append(transaction)

        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))
        else:
            msg_dicts = [json.loads(tx.signature_message_fragment.as_string()) for tx in txs]
            return [msg for msg in msg_dicts if self._within(msg, lon, lat, radius)]

    def find_transactions_local(self):
        return [cs.get_message() for cs in FIVE_STATIONS]

    def get_balance(self, address):
        try:
            response = self.__api.get_balances([Address(address)])
            if "balances" in response:
                return response["balances"][0]
            raise BadApiResponse
        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))

    def _within(self, txd, lon, lat, radius):
        if "long" not in txd or "lat" not in txd:
            return False
        x = float(txd['long']) - lon
        y = float(txd['lat']) - lat
        return x * x + y * y < radius ** 2
