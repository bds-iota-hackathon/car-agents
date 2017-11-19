from tornado_json.requesthandlers import APIHandler
from caragent.model.message import Message
from caragent.model.response import Response


class Search(APIHandler):
    def get(self):
        try:
            lat = self.get_argument("lat", None)
            lon = self.get_argument("lon", None)
            radius = self.get_argument("radius", None)
            if lat is None or lon is None or radius is None:
                print "Something is bad"
                raise Exception("Crap values")

            response = self.application.iota.find_transactions(float(lon), float(lat), float(radius))
        except Exception as e:
            self.set_status(404, "Error: {e}".format(e=e))
        else:
            self.set_status(200, "OK")
            self.write(Response(response).to_json())


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
        bundle = self.application.iota.send_transfer(
            transfers=self.application.iota.create_transfers(
                self.application.address,
                message.to_json()
            ),
            inputs=self.application.iota.create_inputs(self.application.address)
        )

        if bundle is not None:
            self.set_status(200, 'OK')
            return
        self.set_status(404, 'Error')


class Pay(APIHandler):
    def post(self, address):
        pass
