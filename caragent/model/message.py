import time
import json

class Message(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.timestamp = int(time.time())

    def to_json(self):
        return json.dumps(self.__dict__)