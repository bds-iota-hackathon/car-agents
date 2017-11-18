from tornado_json.requesthandlers import APIHandler
from core.iotawrapper import IotaWrapper


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
    def post(self):
        status = self.get_argument('status', None)
        id = self.get_argument('id', None)

        if status is None or id is None:
            self.set_status(404, 'Error')

        iota = IotaWrapper()


class Pay(APIHandler):
    def post(self, address):
        pass
