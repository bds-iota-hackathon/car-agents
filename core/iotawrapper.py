from iota import *
from requests.exceptions import ConnectionError

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IotaWrapper:
    def __init__(self, url, seed):
        self.url = url
        self.seed = seed
        self.node_info = None
        self.api = None

    def connect(self):
        try:
            self.api = Iota(self.url, self.seed)
            self.node_info = self.api.get_node_info()
            logger.info("Node information: {info}".format(info=self.node_info))
        except ConnectionError as e:
            logger.exception("Connection error: {e}".format(e=e))
        except BadApiResponse as e:
            logger.exception("Bad Api Response: {e}".format(e=e))
        else:
            logger.info("Connected.")
            return True
        return False
