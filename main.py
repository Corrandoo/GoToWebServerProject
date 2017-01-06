import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")

settings = [
    ('/', MainHandler)
]

app = tornado.web.Application([])
app.listen(8888)
tornado.ioloop.IOLoop.current().start()