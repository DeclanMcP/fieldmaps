import tornado.ioloop
import tornado.web

class TeamsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("{{ name: 'Bayern Munich' }, { name: 'FC Barcelona'}}");

class StatsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("[[{s: 1.0, c:0.0}, {s: 1.0, c:0.0}], [{s: 1.0, c:0.0}, {s: 1.0, c:0.0}]]");

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/teams", TeamsHandler),
        (r"/stats", StatsHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()