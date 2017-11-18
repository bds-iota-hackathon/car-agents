from tornado_json.requesthandlers import APIHandler
from core.iotawrapper import IotaWrapper
from caragent.model.message import Message


class Search(APIHandler):
    def get(self):
        try:
            lan = self.get_argument('lan', None)
            long = self.get_argument('long', None)
            print lan
            print long
            single_location = dict()
            single_location['time'] = 123213213
            single_location['lan'] = lan
            single_location['long'] = long
            single_location['id'] = 'GFDSAHOFDSHAUFSAZFSAHFFHDSIAHDISAHIDJFDSKAJDSA'
            single_location['time'] = 'TIZODOIHIDSHAUGIDSGAIDSAHODSGIDSAIUDSADSAOI'

            locations = [single_location, single_location]
            return locations

        except:
            self.set_status(404, 'Error')


class UpdateStation(APIHandler):
    def get(self):
        status = self.get_argument('status', None)
        id = self.get_argument('id', None)

        if status is None or id is None:
            self.set_status(404, 'Error')
            return

        message = Message(
            parameters={"id": id, "status": status}
        )

        print message.to_json()

        bundle = self.application.iota.send_transfer(
            transfers=self.application.iota.create_transfers(
                self.application.address,
                message.to_json()
            ),
            inputs=self.application.iota.create_inputs(self.application.address)
        )

        print bundle

        if bundle is not None:
            self.set_status(200, 'OK')
            return
        self.set_status(404, 'Error')


class Pay(APIHandler):
    def post(self, address):
        pass
