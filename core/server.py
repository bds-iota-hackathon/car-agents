import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import tornado
import tornado_json.application
from tornado_json.routes import get_routes
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options

import api
from db import models


class Application(tornado_json.application.Application):
    def __init__(self):

        routes = get_routes(api)
        print("Routes\n======\n\n" + json.dumps(
            [(url, repr(rh)) for url, rh in routes],
            indent=2)
        )

        settings = dict(
            debug=options.debug,
            xsrf_cookies=False,
            # TODO: update manually
            cookie_secret='lpyoGs9/TAuA8IINRTRRjlgBspMDy0lKtvQNGrTnA9g=',
            )
        super(Application, self).__init__(routes=routes, generate_docs=True, settings=settings)

        engine = create_engine('sqlite:///:memory:', echo=True)

        self.db = scoped_session(sessionmaker(bind=engine))

        models.Base.metadata.create_all(engine, checkfirst=True)


def main():
    tornado.options.parse_command_line()

    application = Application()
    application.listen(80)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
