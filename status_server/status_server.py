#!/usr/bin/env python
from random import choice

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

class StatusHandler(RequestHandler):
    def prepare(self):
        status = choice([x for x in self.request.uri.split('/') if x != ''])
        self.set_status(int(status))
        self.write(status)
        self.finish()


def main():
    server = Application([(r'/.*', StatusHandler)])
    server.listen(8888)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
