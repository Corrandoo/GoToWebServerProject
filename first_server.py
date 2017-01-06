import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Привет, мой Господин!")

settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler)
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()