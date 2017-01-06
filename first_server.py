import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<form method ='get' action ='/hello'><input name='name' /></form>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "Анон")
        self.write("<h1>Привет, " + name + "</h1>")


class CatsHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            ('Васька', '/static/cat1.jpg'),
            ('Петька', '/static/cat2.jpg')
        ]
        cat = random.choice(cats)
        self.render("cats.html", cat_name=cat[0], cat_adress=cat[1])


settings = [
    ('/', MainHandler),
    ('/hello', HelloHandler),
    ('/cats', CatsHandler),
    ('/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'})
]
# http://host:port/page/page?param=value&param1=value

app = tornado.web.Application(settings)  # создали веб приложение
app.listen(80)  # слушаем 8888 порт
tornado.ioloop.IOLoop.current().start()  # не отрубаем программу, пока господин этого не захочет