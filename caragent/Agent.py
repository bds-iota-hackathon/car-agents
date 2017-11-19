import json

import tornado
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado_json.application
from tornado_json.routes import get_routes
from core.iotawrapper import IotaWrapper

import agent


class Application(tornado_json.application.Application):
    def __init__(self):

        routes = get_routes(agent)
        print("Routes\n======\n\n" + json.dumps(
            [(url, repr(rh)) for url, rh in routes],
            indent=2)
        )

        settings = dict(
            debug=True,
            xsrf_cookies=False,
            # TODO: update manually
            cookie_secret='lpyoGs9/TAuA8IINRTRRjlgBspMDy0lKtvQNGrTnA9g=',
            )
        super(Application, self).__init__(routes=routes, generate_docs=True, settings=settings)

        self.ulr = "http://p103.iotaledger.net:14700"
        self.address = "OPMGOSBITOTGSZRESXAO9SGPAOOFEQ9OIPEMY9DEHPVOUULUHXIHHWBNFNMKXPEZWIMHB9JPEXSE9SFLA"
        self.seed = "OJJUQWUWCW9LXFBGHIUGXQTUYYOAHJIQMJBBPOHBHCLBYDUMXLNLSUQJLNFMBITGSXGNLPFABLTQDXBM9"

        self.iota = IotaWrapper(self.ulr, self.seed)
        self.iota.connect()

def main():
    tornado.options.parse_command_line()

    application = Application()
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    main()
