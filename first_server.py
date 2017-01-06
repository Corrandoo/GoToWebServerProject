import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Привет, мой Господин!</h1>")

settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler)
]

app = tornado.web.Application(settings)  # создали веб приложение
app.listen(8888)  # слушаем 8888 порт
tornado.ioloop.IOLoop.current().start()  # не отрубаем программу, пока господин этого не захочет