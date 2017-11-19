import json
import time


class Response(object):
    def __init__(self, data):
        self.data = data
        self.timestamp = int(time.time())

    def to_json(self):
        return json.dumps(self.__dict__)